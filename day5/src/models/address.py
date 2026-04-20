#create address class using pydantic
from pydantic import BaseModel, Field
from src.models.customer import Customer
class Address(BaseModel):
    customer:Customer
    customer_id: int = Field(..., gt=0, description="Customer ID must be a positive integer")
    street: str = Field(..., pattern=r'^[a-zA-Z0-9\s\-\,\.]+$', description="Street must be a string")
    city: str = Field(..., pattern=r'^[a-zA-Z\s]+$', description="City must be a string")
    state: str = Field(..., pattern=r'^[a-zA-Z\s]+$', description="State must be a string")
    zip_code: str = Field(..., pattern=r'^\d{5}(-\d{4})?$', description="Zip code must be in the format 12345 or 12345-6789") 
    country: str = Field(..., pattern=r'^[a-zA-Z\s]+$', description="Country must be a string")
    