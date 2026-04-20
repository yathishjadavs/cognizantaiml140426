import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', '..'))

sys.path.append(project_root)
from src.configuration.conf import Config
from src.dataloaders.coustomer_csv_data_loder import CustomerCSVDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl


def display_customer_info(customer_store):
    config = Config()
    evn = config.app_env
    if evn.lower() == "development":
        data_loader = CustomerCSVDataLoader()
        data_loader.load_data(config.get_resource_path(), customer_store)
        for customer in customer_store.get_all_customers():
            print(f"Customer ID: {customer.customer_id}, Name: {customer.name.first_name} {customer.name.last_name}, Email: {customer.email}, Phone: {customer.phone}")
if __name__ == "__main__":
    customer_store = CustomerStoreImpl()
    display_customer_info(customer_store)       
    