#create the company type class using pydantic
from pydantic import BaseModel, Field
from src.models.customer import Customer
from src.models.company_type import CompanyType
class Corporate(Customer):
    company_name: str = Field(..., description="Company name must be a string")
    company_type: CompanyType = Field(..., description="Company type must be one of the defined types")
    