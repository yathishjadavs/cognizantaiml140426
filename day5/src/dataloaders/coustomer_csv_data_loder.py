#creat customer csv data loader implimentation from costumer data loader abstract class
import pandas as pd
from src.dataloaders.coustomer_data_loader import CustomerDataLoader
from src.models.customer import Customer
from src.models.full_name import FullName
from src.stores.customer_store_impl import CustomerStoreImpl

class CustomerCSVDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: 'CustomerStoreImpl'):
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            try:
                customer_id = str(row['customer_id'])
                first_name = row['first_name']
                last_name = row['last_name']
                email = row['email']
                phone_no = int(row['phone_no'])
                customer = Customer(customer_id=customer_id, name=FullName(first_name=first_name, last_name=last_name), email=email, phone=phone_no)
                customer_store.add_customer(customer)
            except (ValueError, KeyError) as e:
                # Skip rows with invalid data
                continue
