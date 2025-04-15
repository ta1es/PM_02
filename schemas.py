from pydantic import BaseModel, Field, EmailStr
from datetime import date


class ClientCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    phone: str = Field(..., min_length=1)


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float
    stock: int


class OrderCreate(BaseModel):
    client_id: int
    product_id: int
    quantity: int
    order_date: date
