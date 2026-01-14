from fastapi import FastAPI, Request, HTTPException
import mysql.connector
import time
from loguru import logger
import sys

# 1. FastAPI 객체 생성
app = FastAPI()

# 2. 로깅 환경 설정
logger.remove()
logger.add(sys.stdout,
           format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>")
logger.add("api.log", rotation="10 MB")


# 3. 미들웨어 설정
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    method = request.method
    url = str(request.url)

    logger.info(f"🚀 [REQUEST] {method} {url}")

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    logger.info(f"✅ [RESPONSE] Status: {response.status_code} | Time: {process_time:.2f}ms")

    return response


# 4. DB 연결 함수 및 경로(Route) 정의
def get_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="tester",
        password="tester",
        database="test_db"
    )


# ---------------------------
# CREATE
# ---------------------------
@app.post("/todos")
async def create_todo(request: Request):
    body = await request.json()
    content = body.get("content")

    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    conn = get_db()
    cursor = conn.cursor()

    # 👉 학생이 작성해야 하는 SQL
    # INSERT 문 작성
    # 예: INSERT INTO todo (content) VALUES (%s)
    cursor.execute(
        ### TODO: 여기에 INSERT SQL 작성 ###
        "INSERT INTO todo (content) VALUES (%s)"
        ,
        (content,)
    )
    conn.commit()

    todo_id = cursor.lastrowid

    # 👉 학생이 작성해야 하는 SQL
    # SELECT 문 작성하여 방금 만든 todo 조회
    cursor.execute(
        ### TODO: 여기에 SELECT SQL 작성 ###
        "SELECT * FROM todo WHERE id = %s"
        ,
        (todo_id,)
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "id": row[0],
        "content": row[1],
        "created_at": str(row[2])
    }


# ---------------------------
# READ
# ---------------------------
@app.get("/todos")
def get_todos():
    conn = get_db()
    cursor = conn.cursor()

    # 👉 학생이 작성해야 하는 SQL
    # 전체 todo 조회 SELECT 문 작성
    cursor.execute(
        ### TODO: 여기에 전체 조회 SELECT SQL 작성 ###
        "SELECT * FROM todo ORDER BY created_at"
    )
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "id": r[0],
            "content": r[1],
            "created_at": str(r[2])
        }
        for r in rows
    ]


# ---------------------------
# DELETE
# ---------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    conn = get_db()
    cursor = conn.cursor()

    # 👉 학생이 작성해야 하는 SQL
    # 삭제 DELETE 문 작성
    cursor.execute(
        ### TODO: 여기에 DELETE SQL 작성 ###
        "DELETE FROM todo WHERE id = %s"
        ,
        (todo_id,)
    )
    conn.commit()

    affected = cursor.rowcount

    cursor.close()
    conn.close()

    if affected == 0:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted"}