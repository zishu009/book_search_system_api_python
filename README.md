# 📚 Book Search API

> A mini-application for a fictional Book Search System built with **Flask**, **SQLAlchemy**, **Marshmallow**

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- SQLAlchemy
- Marshmallow
- SQLite (books.db)

---

## 🚀 Project Structure

```
book_search_api/
│
├── app.py          # Main Flask application
├── models.py       # SQLAlchemy models and database setup
├── schemas.py      # Marshmallow schemas for request validation
├── books.db        # SQLite database
├── routes.py       # API set up
├── create_db.py    # Create the database and add some data into it
```
---

## 🧩 Setup Instructions

### 1. Create a virtual environment (optional but recommended)

```bash
py -m venv .env
.\.env\Scripts\Activate.ps1  # Activate Virtual Enviornment
```

### 3. Install dependencies

```bash
pip install flask
pip install flask_sqlalchemy
pip install marshmallow
```

### 4. Create the database and then Run the application

```bash
python create_db.py
python app.py
```

The API will be available at:  
👉 `http://localhost:5000`

---

## 📚 API Endpoints

### 1. **GET /books**

- **Description**: Fetch all books.
- **Method**: `GET`
- **Example Request**:
  ```
  GET http://localhost:5000/books
  ```
- **Success Response** (`200 OK`):
```json
[
  {
    "id": 1,
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian",
    "year": 1949
  },
  ...
]
```

---

### 2. **POST /query**

- **Description**: Send a prompt to the Book Assistant and receive a generated response.
- **Method**: `POST`
- **Request Body**:
```json
{
  "prompt": "Suggest me a mystery book"
}
```
- **Success Response** (`200 OK`):
```json
{
  "response": "📚 Book Assistant says: Based on your prompt 'Suggest me a mystery book', here are some suggestions!"
}
```
- **Validation**:
  - Missing or invalid `prompt` field returns `400 Bad Request`.

---

## 🗄️ Database Schema

The SQLite database `books.db` contains one table:

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    genre TEXT,
    year INTEGER
);
```

---

## 🔎 SQL Queries Executed via SQLAlchemy

The application supports SQL operations using SQLAlchemy:

- **Fetch all books by genre**
- **Count the number of books by a specific author**
- **Find books published after a certain year**

Example functions implemented in Python using SQLAlchemy sessions.

---

## 🚦 Error Handling

- Proper HTTP status codes are returned (`200 OK`, `400 Bad Request`, `500 Internal Server Error`).
- Marshmallow is used for request validation.
- Errors are captured and appropriate responses are sent.


