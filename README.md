# friday-13
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![REST API](https://img.shields.io/badge/-REST%20API-464646?style=flat-square&logo=REST%20API)](https://restfulapi.net/)
[![PostgreSQL](https://img.shields.io/badge/-SQLite-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

Friday-13 является сервисом для работы в кандидатами и резюме.

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone https://github.com/vtolstopyatov/friday-13
```

### Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

### Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Запуск проекта:

```
docker-compose up -d --build
```

### Работа с API через Postman Agent:

#### Для получения всех кандидатов:

```
GET http://130.193.38.180/api/applicants/
```
#### Для получения кандидатов по id:
```
GET http://130.193.38.180/api/applicants/{id}/
```

#### Для получения всех городов:
```
GET http://130.193.38.180/api/cities/
```
#### Для получения городов по id:
```
GET http://130.193.38.180/api/cities/{id}/
```

#### Для получения всех языков:
```
GET http://130.193.38.180/api/languages/
```
#### Для получения языков по id:
```
GET http://130.193.38.180/api/languages/{id}/
```

#### Для получения всех вакансий:
```
GET http://130.193.38.180/api/vacancies/
```
#### Для получения вакансий по id:
```
GET http://130.193.38.180/api/vacancies/{id}/
```
#### Для создания вакансий:
```
POST http://130.193.38.180/api/vacancies/
JSON:
{ 
  "title": "Программист Java", 
  "expirience": "LOW", 
  "conditions": "Удаленная работа, гибкий график", 
  "grade": "IN", 
  "work_format": "FD", 
  "description": "Ищем Java-разработчика для разработки и поддержки наших Java-приложений.", 
  "requirements": "Требования: знание Java, основы алгоритмов и структур данных, ответственность.", 
  "optional_requirements": "Дополнительные требования: опыт работы с Spring Framework, знание SQL.", 
  "responsibility": "Обязанности: разработка и тестирование Java-приложений, участие в планировании проектов.", 
  "selection_stages": "Этапы отбора: рассмотрение резюме, техническое собеседование, выполнение тестового задания.", 
  "is_active": true, 
  "is_archive": false, 
  "created": "2023-10-29T15:30:00Z", 
  "city": 1, 
  "min_wage": 60000, 
  "max_wage": 90000, 
  "currency": "RUB", 
  "language": [ 
    { 
        "id": 1, 
      "level": "A1"
    } 
  ]   
}
```
#### PUT/PATCH вакансий:
```
PUT/PATCH http://130.193.38.180/api/vacancies/{id}/
JSON:
{ 
  "title": "Программист Java", 
  "expirience": "LOW", 
  "conditions": "Удаленная работа, гибкий график", 
  "grade": "IN", 
  "work_format": "FD", 
  "description": "Ищем Java-разработчика для разработки и поддержки наших Java-приложений.", 
  "requirements": "Требования: знание Java, основы алгоритмов и структур данных, ответственность.", 
  "optional_requirements": "Дополнительные требования: опыт работы с Spring Framework, знание SQL.", 
  "responsibility": "Обязанности: разработка и тестирование Java-приложений, участие в планировании проектов.", 
  "selection_stages": "Этапы отбора: рассмотрение резюме, техническое собеседование, выполнение тестового задания.", 
  "is_active": true, 
  "is_archive": false, 
  "created": "2023-10-29T15:30:00Z", 
  "city": 1, 
  "min_wage": 60000, 
  "max_wage": 90000, 
  "currency": "RUB", 
  "language": [ 
    { 
        "id": 1, 
      "level": "A1"
    } 
  ]   
}
```
#### Удаление вакансий:
```
DELETE http://130.193.38.180/api/vacancies/{id}/
```

#### Для получения статуса кандидатов по id:
```
GET http://130.193.38.180/api/vacancies/{vacancy_pk}/responses/
```
#### Добавление статуса кандидатам по id:
```
POST http://130.193.38.180/api/vacancies/{vacancy_pk}/responses/
JSON:
{
    "applicant": 0,
    "vacancy": 0,
    "status": "Отклик"
}

```

#### Для получения статуса кандидата по id:
```
GET http://130.193.38.180/api/vacancies/{vacancy_pk}/responses/{id}/
```
#### PUT/PATCH статуса кандидата по id:
```
PUT/PATCH http://130.193.38.180/api/vacancies/{vacancy_pk}/responses/{id}/
JSON:
{
    "applicant": 0,
    "vacancy": 0,
    "status": "Отклик"
}
```
#### Удалить связь кандидата с вакансией:
```
DELETE http://130.193.38.180/api/vacancies/{vacancy_pk}/responses/{id}/
```

# Над проектом работали:
- [Владимир Толстопятов](https://github.com/vtolstopyatov)
- [Дмитрий Луконин](https://t.me/folite999)
