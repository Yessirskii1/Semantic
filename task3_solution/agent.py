import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()




@tool
def calculate_bmi(weight_kg: float, height_cm: float) -> str:
    h = height_cm / 100
    bmi = round(weight_kg / (h ** 2), 1)
    if bmi < 18.5: cat = "недостаточный вес"
    elif bmi < 25: cat = "норма"
    elif bmi < 30: cat = "избыточный вес"
    else: cat = "ожирение"
    return f"ИМТ: {bmi} ({cat})"


@tool
def calculate_calories(weight_kg: float, height_cm: float, age: int, gender: str, activity: str) -> str:
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + (5 if gender.lower() == "мужской" else -161)
    factors = {"низкая": 1.2, "средняя": 1.55, "высокая": 1.725}
    return f"Норма калорий: ~{int(bmr * factors.get(activity.lower(), 1.2))} ккал/день"





SYSTEM_PROMPT = """Ты — профессиональный фитнес-тренер.
Помогаешь анализировать параметры тела, считать калории и давать рекомендации.
Используй инструменты для получения данных перед ответом.
Если вопрос не связан с фитнесом, здоровьем или питанием — ответь строго: "Команда неизвестна".
Отвечай кратко, на русском языке."""

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),      # переменное окружение
)

tools = [calculate_bmi, calculate_calories]

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder("chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)


def ask(question: str) -> str:
    return agent_executor.invoke({"input": question})["output"]





if __name__ == "__main__":
    print("Тест\n")
    print(ask("Рассчитай ИМТ для веса 75 кг и роста 180 см"))
    print()
    print(ask("Калории для мужчины 30 лет, 80 кг, 175 см, средняя активность"))
    print()
    print(ask("Напиши стихотворение про котов"))
