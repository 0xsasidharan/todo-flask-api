# ✅ To Do Flask API

A simple and extendable RESTful API for managing tasks, built with **Python Flask**.  
The API allows users to create, update, delete, and filter tasks, while tracking stats such as completed and overdue tasks.  
It uses **Flask-Smorest**, **MethodView**, and **Marshmallow** for input validation and clean routing.

---

## 📝 Features

- Full CRUD for Tasks
- Filter tasks by `completed` status
- Track stats: total, completed, pending, overdue
- Input validation using Marshmallow
- RESTful structure using Blueprints and MethodView
- OpenAPI documentation via Flask-Smorest
- Docker support
- Database Integration
- JWT Authentication 

---

## 🚧 Project Progress Checklist

| Day | Feature                                | Status    |
|-----|----------------------------------------|-----------|
| 1   | Basic Flask App with GET, POST, DELETE | ✅ Done   |
| 2   | Add PUT for updating tasks             | ✅ Done   |
| 3   | Filter tasks by `completed` status     | ✅ Done   |
| 4   | Add task statistics `/stats` route     | ✅ Done   |
| 5   | Refactor with Blueprints & MethodView  | ✅ Done   |
| 6   | Add Marshmallow Schemas                | ✅ Done   |
| 7   | Add Flask-Smorest (Swagger docs)       | ✅ Done   |
| 8   | Add Docker Containerization            | ✅ Done   |
| 9   | Database Integration                   | ✅ Done   |
| 10  | JWT Authentication                     | ⬜ Pending |

---

## 📘 API Endpoints

### `GET /tasks`

**Description:** Retrieve all tasks. Optionally filter by completion status.

**Query Parameters:**
- `completed` (optional): `"true"` or `"false"` (case-insensitive)

**Responses:**
- `200 OK`: List of tasks.
- `400 Bad Request`: If an invalid query param is passed.

---

### `POST /tasks`

**Description:** Create a new task.

**Request Body (JSON):**
```json
{
  "title": "Finish project",
  "description": "Submit before Friday",
  "due_date": "15-06-2025",
  "completed": false
}
````

**Responses:**

* `201 Created`: Created task with `task_id` and `created_at`.
* `400 Bad Request`: If input data is invalid or `due_date` format is wrong.

---

### `GET /tasks/<task_id>`

**Description:** Retrieve a task by ID.

**URL Parameters:**

* `task_id`: Task UUID

**Responses:**

* `200 OK`: Task object.
* `400 Bad Request`: If task ID is not found.

---

### `PUT /tasks/<task_id>`

**Description:** Update an existing task.

**Request Body (JSON):**

```json
{
  "title": "Updated title",
  "description": "Updated description",
  "due_date": "20-06-2025",
  "completed": true
}
```

**Responses:**

* `200 OK`: Updated task.
* `400 Bad Request`: If task ID not found or invalid data.

---

### `DELETE /tasks/<task_id>`

**Description:** Delete a task by its ID.

**Responses:**

* `200 OK`: Task deleted message.
* `400 Bad Request`: If task ID is not found.

---

### `GET /stats`

**Description:** Get task summary stats: total, completed, pending, and overdue tasks.

**Responses:**

```json
{
  "total_tasks": 4,
  "completed": 2,
  "pending": 1,
  "overdue": 1
}
```

* `200 OK`: Task statistics.

---

# 🔧 Local Installation

## 📦 Using Python (venv)

### Create virtual environment & activate

```bash
python -m venv venv
venv\Scripts\activate 
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
flask run
```

---

## 🐳 Using Docker

### Build Docker image

```bash
docker build -t todo-flask-api .
```

### Run container

```bash
docker run -p 5000:5000 todo-flask-api
```

### Run multiple containers using docker-compose

```bash
docker-compose up --build
```




