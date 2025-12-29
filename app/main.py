from fastapi import FastAPI
from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal
from models import Product

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products")
def create_product(name: str, price: float, db: Session = Depends(get_db)):
    product = Product(name=name, price=price)
    db.add(product)
    db.commit()
    return product