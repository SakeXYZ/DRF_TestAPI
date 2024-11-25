# Women API

This project is a RESTful API built with Django and Django REST Framework (DRF) for managing a collection of "Women" entities. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on the "Women" model and integrates with a "Category" model for additional functionality.

## Features

- **GET**: Retrieve a list of all posts or a specific post by ID.
- **POST**: Create a new post.
- **PUT**: Update an existing post by ID.
- **DELETE**: Delete a post by ID.

The project includes both serializers for data validation and model manipulation, as well as views for handling HTTP requests.

---

## Models

### Women
- `title` (CharField): Title of the post (max 255 characters).
- `content` (TextField): Content of the post.
- `time_create` (DateTimeField): Timestamp when the post was created.
- `time_update` (DateTimeField): Timestamp when the post was last updated.
- `is_published` (BooleanField): Indicates if the post is published (default: `True`).
- `cat` (ForeignKey): Foreign key to the `Category` model.

### Category
- `name` (CharField): Name of the category (max 100 characters).

---

## API Endpoints

### Base URL
`/api/v1/womenlist/`

### Endpoints

#### 1. Get All Posts
**URL**: `/api/v1/womenlist/`  
**Method**: `GET`  
**Description**: Retrieves a list of all posts.  
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

#### 2. Get Post by ID
**URL**: `/api/v1/womenlist/<int:pk>/`  
**Method**: `GET`  
**Description**: Retrieves a single post by its ID.  
**Response**: Same as above.

#### 3. Create a New Post
**URL**: `/api/v1/womenlist/`  
**Method**: `POST`  
**Request Body**:
```json
{
  "title": "New Post",
  "content": "New content",
  "is_published": true,
  "cat_id": 1
}
```
**Response**:
```json
{
  "post": {
    "title": "New Post",
    "content": "New content",
    "time_create": "2024-11-25T10:00:00Z",
    "time_update": "2024-11-25T10:00:00Z",
    "is_published": true,
    "cat_id": 1
  }
}
```

#### 4. Update a Post by ID
**URL**: `/api/v1/womenlist/<int:pk>/`  
**Method**: `PUT`  
**Request Body**: Same as `POST`.  
**Response**: Updated post object.

#### 5. Delete a Post by ID
**URL**: `/api/v1/womenlist/<int:pk>/`  
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
   git clone https://github.com/yourusername/women-api.git
   cd women-api
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

- Navigate to the API endpoints using tools like Postman or curl.
- Example request:
  ```bash
  curl -X GET http://127.0.0.1:8000/api/v1/womenlist/
  ```

---

## File Structure

- `models.py`: Defines the `Women` and `Category` models.
- `views.py`: Contains the `WomanAPIView` for handling API requests.
- `serializers.py`: Defines the `WomanSerializer` for validating and serializing data.
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

Feel free to customize this description based on your specific repository setup or preferences!
