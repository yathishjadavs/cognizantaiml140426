#create customer class using pydantic
from pydantic import BaseModel, Field,EmailStr
from src.models.full_name import FullName
class Customer(BaseModel):
    customer_id: str = Field(..., description="Customer ID")
    name: FullName = Field(..., description="Name must be a valid full name")
    email: EmailStr = Field(..., description="Invalid email format")
    phone:int = Field(...,ge=1000000000,le=9999999999, description="Phone number must be a positive integer")