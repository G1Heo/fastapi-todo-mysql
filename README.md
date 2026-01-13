# FastAPI Todo List 실습

## 🚀 프로젝트 개요
Docker를 활용해 MySQL 데이터베이스를 독립적인 컨테이너로 실행하고, FastAPI 서버와 연동하여 실제 데이터가 저장되는 흐름을 학습하기 위한 프로젝트입니다.

## 🛠 사용 기술
- **Backend:** FastAPI, Uvicorn
- **Database:** MySQL 8.0 (Dockerized)
- **DB Driver:** PyMySQL
- **Tools:** Docker Compose, Postman, Adminer

## 📋 주요 기능
- `POST /todos`: 새로운 할 일 추가 (DB INSERT)
- `GET /todos`: 전체 할 일 목록 조회 (DB SELECT)
- `DELETE /todos/{id}`: 특정 할 일 삭제 (DB DELETE)

---

# FastAPI Todo List Lab

## 🚀 Project Overview
This project is designed to understand the full development workflow of building a backend service. It focuses on establishing a persistent data storage system by connecting a **FastAPI** server with a **Docker-managed MySQL** database.

## 🛠 Tech Stack
- **Backend:** FastAPI, Uvicorn
- **Database:** MySQL 8.0 (Containerized via Docker)
- **Database Driver:** PyMySQL
- **DevOps & Tools:** Docker Compose, Postman, Adminer



## 📋 Key Features
- **Create Todo (`POST /todos`):** Receives a JSON payload and inserts a new task into the MySQL database.
- **Read All Todos (`GET /todos`):** Fetches the complete list of tasks from the database.
- **Delete Todo (`DELETE /todos/{id}`):** Removes a specific task from the database using its unique ID provided in the URL path.

## ⚙️ How to Run
1. **Infrastructure Setup:** Run the database container.
   ```bash
   docker compose up -d
   ```

2. **Server Startup**: Run the FastAPI application using uv.
   ```bash
   uv run uvicorn main:app --reload
   ```
  
3. API Testing: Use Postman or the built-in Swagger UI at http://localhost:8000/docs.

