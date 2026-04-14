# creating the entry point
import faker
from store.customerstore import CustomerStore
from view.customerviwe import CustomerView

"""
creating entry point for the application to display a random name. this is the fille
that will be executed when we run the application. it will use the faker library to generate a random name and print it to the console.
"""


def run():
    """
    this function will be called when the application is run. it will generate a random name and print it to the console.
    """
    customer_store = CustomerStore()
    customer_store.generate_customers()
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()


if __name__ == "__main__":
    run()
