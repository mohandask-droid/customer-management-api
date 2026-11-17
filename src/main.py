from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from src.database import get_db

app = FastAPI(title="Customer Management API")


@app.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok"}