#generate 100 customera
import faker
import typing
from models.customer import Customer
class CustomerStore:
    def __init__(self):
        self.customers = []
        self.faker = faker.Faker()

    def generate_customers(self, num_customer:int=100):
        for _ in range(num_customer):
            name = self.faker.name()
            email = self.faker.email()
            dob = self.faker.date_of_birth()
            customer = Customer(name, email, dob)
            self.customers.append(customer)

    def get_customers(self):
        return self.customers