# To-Do List API Documentation

## Introduction
The **To-Do List API** is a RESTful web service built using FastAPI that allows users to manage their tasks. This API supports adding, retrieving, updating, and deleting tasks. It interacts with a SQLite database for persistent task storage.

## Technologies Used
- **FastAPI**: For building the API
- **SQLite**: For database storage
- **Pydantic**: For data validation
- **SQLAlchemy**: For database interactions
- **Uvicorn**: ASGI server for running FastAPI applications

## Project Structure
```bash
todos-app
 ┣ app
 ┃ ┣ models
 ┃ ┃ ┣ task.py         # Database models
 ┃ ┣ routes
 ┃ ┃ ┣ task.py         # API endpoints
 ┃ ┣ schemas
 ┃ ┃ ┣ task.py         # Pydantic schemas
 ┃ ┣ config.py         # Configuration settings
 ┃ ┣ database.py       # Database setup
 ┃ ┣ main.py           # Entry point of the application
 ┗ tasks.db            # SQLite database
```

## API Endpoints

### 1. **Create a Task**
**Endpoint:** `POST /tasks`

**Request Body:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, and bread"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, and bread",
  "completed": false
}
```

### 2. **Retrieve All Tasks**
**Endpoint:** `GET /tasks`

**Response:**
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, and bread",
    "completed": false
  }
]
```

### 3. **Update a Task**
**Endpoint:** `PUT /tasks/{task_id}`

**Request Body:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread, and cheese",
  "completed": true
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread, and cheese",
  "completed": true
}
```

### 4. **Delete a Task**
**Endpoint:** `DELETE /tasks/{task_id}`

**Response:**
```json
{"message": "Task deleted successfully"}
```

## Error Handling
- **400 Bad Request**: If input data is invalid.
- **404 Not Found**: If a task with the given ID does not exist.

## Running the API
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the FastAPI application:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Access API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## After Cloning Instructions
If you clone this repository, follow these steps to set up and run the project:

1. **Navigate to the project directory**
   ```bash
   cd todos-app
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python app/database.py  # Run this only if migrations are needed
   ```

5. **Run the FastAPI application**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API Docs**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Conclusion
This API provides a simple yet functional way to manage a to-do list. It is scalable, easy to extend, and well-documented with automatic documentation from FastAPI.

