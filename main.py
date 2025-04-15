from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
import database


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/clients/")
def create_client(
    client: schemas.ClientCreate,
    db: Session = Depends(get_db)
):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


@app.post("/products/")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.post("/orders/")
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@app.get("/clients/")
def get_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()


@app.get("/products/")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


@app.get("/orders/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()
