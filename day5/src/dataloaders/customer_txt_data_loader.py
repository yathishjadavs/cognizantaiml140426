from dataloaders.coustomer_data_loader import CustomerDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl
from src.models.customer import Customer
from src.models.full_name import FullName
class CustomerTXTDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: 'CustomerStoreImpl'):
        with open(file_path, 'r') as file:
            customer_data = {}
            for line in file:
                line = line.strip()
                if not line or line == "--------------------------------":
                    if customer_data and 'customer_id' in customer_data:
                        customer = Customer(
                            customer_id=customer_data['customer_id'],
                            name=FullName(first_name=customer_data['first_name'], last_name=customer_data['last_name']),
                            email=customer_data['email'],
                            phone=int(customer_data['phone_no'])
                        )
                        customer_store.add_customer(customer)
                    customer_data = {}
                    continue
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    customer_data[key] = value
            # Don't forget the last customer if file doesn't end with separator
            if customer_data and 'customer_id' in customer_data:
                customer = Customer(
                    customer_id=customer_data['customer_id'],
                    name=FullName(first_name=customer_data['first_name'], last_name=customer_data['last_name']),
                    email=customer_data['email'],
                    phone=int(customer_data['phone_no'])
                )
                customer_store.add_customer(customer)