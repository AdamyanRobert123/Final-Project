from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    unit = Column(String, nullable=False)
    description = Column(String)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)
    contact_person = Column(String)


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    quantity = Column(Integer, nullable=False)
    delivery_date = Column(Date)

    product = relationship("Product")
    customer = relationship("Customer")

