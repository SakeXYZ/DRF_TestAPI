## English Version

# Record Management API

This project is a RESTful API built with Django and Django REST Framework (DRF) for managing records. The API provides CRUD (Create, Read, Update, Delete) operations for records and integrates with a category model for additional functionality.

---

## Features

- **GET**: Retrieve a list of all records or a specific record by ID.
- **POST**: Create a new record.
- **PUT**: Update an existing record by ID.
- **DELETE**: Delete a record by ID.

---

## Models

### Record
- `title` (CharField): The title of the record (max 255 characters).
- `content` (TextField): The content of the record.
- `time_create` (DateTimeField): Timestamp of when the record was created.
- `time_update` (DateTimeField): Timestamp of the last update.
- `is_published` (BooleanField): Indicates if the record is published (default: `True`).
- `cat` (ForeignKey): Foreign key to the `Category` model.

### Category
- `name` (CharField): The name of the category (max 100 characters).

---

## API Endpoints

### Base URL
`/api/v1/recordlist/`

### Endpoints

#### 1. Get All Records
**URL**: `/api/v1/recordlist/`  
**Method**: `GET`  
**Description**: Retrieves a list of all records.  
**Response**:  
```json
{
  "posts": [
    {
      "title": "Sample Title",
      "content": "Sample Content",
      "time_create": "2024-11-25T10:00:00Z",
      "time_update": "2024-11-25T10:00:00Z",
      "is_published": true,
      "cat_id": 1
    }
  ]
}
```

#### 2. Get Record by ID
**URL**: `/api/v1/recordlist/<int:pk>/`  
**Method**: `GET`  
**Description**: Retrieves a single record by its ID.  
**Response**: Same as above.

#### 3. Create a New Record
**URL**: `/api/v1/recordlist/`  
**Method**: `POST`  
**Request Body**:
```json
{
  "title": "New Record",
  "content": "New content",
  "is_published": true,
  "cat_id": 1
}
```
**Response**:
```json
{
  "post": {
    "title": "New Record",
    "content": "New content",
    "time_create": "2024-11-25T10:00:00Z",
    "time_update": "2024-11-25T10:00:00Z",
    "is_published": true,
    "cat_id": 1
  }
}
```

#### 4. Update a Record by ID
**URL**: `/api/v1/recordlist/<int:pk>/`  
**Method**: `PUT`  
**Request Body**: Same as `POST`.  
**Response**: Updated record object.

#### 5. Delete a Record by ID
**URL**: `/api/v1/recordlist/<int:pk>/`  
**Method**: `DELETE`  
**Response**:
```json
{
  "post": "delete post <pk>"
}
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/record-api.git
   cd record-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Usage

- Use tools like Postman or curl to interact with the API.
- Example request:
  ```bash
  curl -X GET http://127.0.0.1:8000/api/v1/recordlist/
  ```

---

## File Structure

- `models.py`: Contains the `Record` and `Category` models.
- `views.py`: Implements the API views for handling requests.
- `serializers.py`: Defines serializers for validation and serialization.
- `urls.py`: Maps endpoints to views.

---

## Technologies

- **Python** (v3.10+)
- **Django** (v4.2+)
- **Django REST Framework** (v3.14+)

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

---

## Версия на русском

# API для управления записями

Этот проект представляет собой RESTful API, разработанный с использованием Django и Django REST Framework (DRF), для управления записями. API предоставляет функции CRUD (создание, чтение, обновление, удаление) для записей и взаимодействует с моделью категорий для дополнительной функциональности.

---

## Возможности

- **GET**: Получение списка всех записей или конкретной записи по ID.
- **POST**: Создание новой записи.
- **PUT**: Обновление существующей записи по ID.
- **DELETE**: Удаление записи по ID.

---

## Модели

### Record
- `title` (CharField): Название записи (максимум 255 символов).
- `content` (TextField): Содержание записи.
- `time_create` (DateTimeField): Время создания записи.
- `time_update` (DateTimeField): Время последнего обновления записи.
- `is_published` (BooleanField): Опубликована ли запись (по умолчанию: `True`).
- `cat` (ForeignKey): Внешний ключ на модель `Category`.

### Category
- `name` (CharField): Название категории (максимум 100 символов).

---

## Конечные точки API

### Базовый URL
`/api/v1/recordlist/`

### Конечные точки

#### 1. Получить все записи
**URL**: `/api/v1/recordlist/`  
**Метод**: `GET`  
**Описание**: Возвращает список всех записей.  
**Ответ**:  
```json
{
  "posts": [
    {
      "title": "Пример названия",
      "content": "Пример содержания",
      "time_create": "2024-11-25T10:00:00Z",
      "time_update": "2024-11-25T10:00:00Z",
      "is_published": true,
      "cat_id": 1
    }
  ]
}
```

#### 2. Получить запись по ID
**URL**: `/api/v1/recordlist/<int:pk>/`  
**Метод**: `GET`  
**Описание**: Возвращает запись по её ID.  
**Ответ**: То же самое, что и выше.

#### 3. Создать новую запись
**URL**: `/api/v1/recordlist/`  
**Метод**: `POST`  
**Тело запроса**:
```json
{
  "title": "Новая запись",
  "content": "Новое содержание",
  "is_published": true,
  "cat_id": 1
}
```
**Ответ**:
```json
{
  "post": {
    "title": "Новая запись",
    "content": "Новое содержание",
    "time_create": "2024-11-25T10:00:00Z",
    "time_update": "2024-11-25T10:00:00Z",
    "is_published": true,
    "cat_id": 1
  }
}
```

#### 4. Обновить запись по ID
**URL**: `/api/v1/recordlist/<int:pk>/`  
**Метод**: `PUT`  
**Тело запроса**: То же, что и для `POST`.  
**Ответ**: Обновлённый объект записи.

#### 5. Удалить запись по ID
**URL**: `/api/v1/recordlist/<int:pk>/`  
**Метод**: `DELETE`  
**Ответ**:
```json
{
  "post": "удалена запись <pk>"
}
```

---

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/record-api.git
   cd record-api
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Примените миграции:
   ```bash
   python manage.py migrate
   ```

4. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

---

## Использование

- Используйте инструменты, такие как Postman или curl, для взаимодействия с API.
- Пример запроса:
  ```bash
  curl -X GET http://127.0.0.1:8000/api/v1/recordlist/
  ```

---

## Структура проекта

- `models.py`: Содержит модели `Record` и `Category`.
- `views.py`: Реализует API для обработки запросов.
- `serializers.py`: Определяет сериализаторы для проверки и сериализации данных.
