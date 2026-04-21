#create configuration file for the application
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class Config(BaseModel):
    app_env: str = Field(default_factory=lambda: os.getenv("APP_ENV", "development"))
    
    def get_resource_path(self) -> str:
        if self.app_env.lower() == "production":
            return f"src/resources/coustomers.json"
        elif self.app_env.lower() == "development":
            return f"src/resources/customers.csv"
        elif self.app_env.lower() == "testing":
            return f"src/resources/coustomers.txt"
        else:
            print(f"Invalid APP_ENV value: {self.app_env}")
            return f"src/resources/customers.csv"
