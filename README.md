# Library System API

This project is a simple CRUD (Create, Read, Update, Delete) API for managing a list of books in a library. It's built using Django and Django REST Framework (DRF).

## Features

- Create, Read, Update, and Delete books
- List all books with pagination
- Search books by title or author
- Retrieve book details by ID

## Prerequisites

- Python 3.8+
- pip
- virtualenv (optional, but recommended)

## Setup

1. Clone the repository:
   ```
   https://github.com/Jazze7/crud-book-visics-backend.git
   cd xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxcrud-book-visics-backend
   ```

2. Create and activate a virtual environment (optional):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/api/`.

## API Endpoints

- List all books: GET `/api/books/`
- Search book: GET `/api/books/?search=`
- Create a new book: POST `/api/books/create-book/`
- Retrieve a specific book: GET `/api/books/view-book/<id>/`
- Update a book: PUT `/api/books/update-book/<id>/`
- Delete a book: DELETE `/api/books/delete-book/<id>/`

## Usage Examples

### List all books

```
GET /api/books/
```

Response:
```json
{
  "status_code": 200,
  "data": [
    {
      "id": 1,
      "title": "Django for Beginners",
      "author": "William S. Vincent",
      "published_date": "2020-01-01",
      "isbn": "1234567890123",
      "price": "29.99",
      "stock": 10
    },
    // ... more books ...
  ],
  "pagination": {
    "count": 20,
    "next": "http://127.0.0.1:8000/api/books/?page=2",
    "previous": null
  }
}
```

### Create a new book

```
POST /api/books/
Content-Type: application/json

{
  "title": "Python Crash Course",
  "author": "Eric Matthes",
  "published_date": "2019-05-03",
  "isbn": "1593279280123",
  "price": 39.99,
  "stock": 15
}
```

Response:
```json
{
  "status_code": 201,
  "message": "Successfully added product",
  "data": {
    "id": 2,
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "published_date": "2019-05-03",
    "isbn": "1593279280123",
    "price": "39.99",
    "stock": 15
  }
}
```

## Error Handling

The API returns appropriate HTTP status codes and error messages in JSON format for common exceptions.

Example error response:
```json
{
  "status_code": 400,
  "message": "validation error",
  "error": {
    "isbn": ["Ensure this field has no more than 13 characters."]
  }
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
