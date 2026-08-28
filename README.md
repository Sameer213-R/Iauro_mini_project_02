# Iauro Mini Project 02

## Flask + PostgreSQL CRUD Application with Docker

This project is a containerized CRUD application developed using **Python Flask** and **PostgreSQL**. Docker Compose is used to run the Flask application and PostgreSQL database as separate containers.

The application provides REST API endpoints to perform **Create, Read, Update, and Delete (CRUD)** operations on the `users` table.

---

## 1. Project Objective

The main objective of this project is to build a simple backend application where:

- Flask provides the REST API.
- PostgreSQL stores the application data.
- Docker containerizes the Flask application.
- Docker Compose manages Flask and PostgreSQL together.
- Database connection logic is separated from the application.
- API routes are separated from business/database logic.
- PostgreSQL tables are initialized using `init.sql`.

This structure makes the application easier to understand, maintain, and extend.

---

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | REST API framework |
| PostgreSQL | Database |
| Psycopg2 | PostgreSQL connection from Python |
| Docker | Containerization |
| Docker Compose | Multi-container application |
| Git/GitHub | Version control |

---

## 3. Project Structure

```text
containerized-applications/
│
├── Flask_app/
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── connection.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── services.py
│   │
│   └── app.py
│
├── postgreSQL/
│   └── init.sql
│
├── docker-compose.yml
├── docker_command.txt
├── .gitignore
└── README.md