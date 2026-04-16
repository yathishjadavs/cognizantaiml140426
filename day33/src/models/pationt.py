"""
create patioent """
import typing
import datetime
class Patient:
    def __init__(self, id: int, name: str, age: int, phone: str,specialization:str,dob:datetime.date):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.specialization = specialization
        self.dob = dob
        



    def __str__(self):
        return f"Patient {self.name} (ID: {self.id}), Age: {self.age}, Phone: {self.phone}, Specialization: {self.specialization}, Date of Birth: {self.dob}"