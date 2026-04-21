from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    __tablename__ = "product"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),nullable=False,index=True)
    description = Column(Text)
    price = Column(Float,nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"),nullable=False)
    image_url = Column(String(255))
    created_at = DateTime(DateTime,default=datetime.utcnow)

    category = relationship("Category",back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name})>, price={self.price}"

