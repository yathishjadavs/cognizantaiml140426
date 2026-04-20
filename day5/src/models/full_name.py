#data validation for full name
from pydantic import BaseModel, Field
class FullName(BaseModel):
    first_name: str = Field(..., pattern="^[A-Za-z]+$", description="First name must contain only letters")
    last_name: str = Field(..., pattern="^[A-Za-z]+$", description="Last name must contain only letters")