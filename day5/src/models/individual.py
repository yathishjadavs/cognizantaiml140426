#create class individual using pydantic
from pydantic import BaseModel, Field
from pydantic import Field_validator
from datetime import date
from src.models.customer import Customer    
from src.models.gender import Gender
class Individual(Customer):
    gender: Gender
    dob: date = Field(..., description="Date of Birth must be a valid date")
    @Field_validator('dob')
    def validate_dob(cls, value):
        if value >= date.today():
            raise ValueError("Date of Birth must be in the past")
        age = (date.today() - value).days // 365
        if age < 18:
            raise ValueError("Individual must be at least 18 years old")
        return value
