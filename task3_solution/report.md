# Langchain Агент.

## Стек
- Langchain
- Langchaim-groq
- Fastapi + Uvicorn


## Конфиг ашента
Агент настроен на  роль проффесионального фитнес тренера, ему даны следующие инструкции.
- Использовать tools для точных расчетов
- Отвечать кратко и строго.
- Отклонять не целевые запросы

  ## Tools
  ### calculate_bmi
  Расчитывает индекс массы тела на основании входных данных - вес и рост.
  Формула - вес/(рост*рост)

  ### calculate_calories
  Расчитывает суточную норму калорий по формуле Сан-Жеора, вхлдные данные - вес, рост, возраст, пол, активность.
  
  
## Мини сервис
Мини сервис на базе FastApi.

- Получаем данные в формате JSON через HTTP POST
- Вызывает функццию агента ask() которая обращается к LLM инструментам
- Возвращает результат в формате JSON

## Ообработка неккоректных запросов
<img width="1842" height="1017" alt="subaru" src="https://github.com/user-attachments/assets/c4b3a46a-8d04-4c18-9c21-deca73f44272" />

## Расчет ИМТ
<img width="1864" height="1063" alt="имт" src="https://github.com/user-attachments/assets/75e1a353-cf9f-4166-af2c-1253f3648ad8" />

## Расчет калорий
<img width="1855" height="1055" alt="расчет калорий" src="https://github.com/user-attachments/assets/8215642f-fdd4-429d-bf13-74a4f90fe1e1" />

## Целевой запрос
<img width="1830" height="1061" alt="как набрать массу" src="https://github.com/user-attachments/assets/ddb4421b-ddf1-456a-bb59-b5b2935ce279" />

## Целевой запрос
<img width="1909" height="1057" alt="базуки " src="https://github.com/user-attachments/assets/569f26fb-0725-482f-8de7-564fe3da4e58" />




