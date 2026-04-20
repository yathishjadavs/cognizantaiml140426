#create customer data loader abstract class abc import ABC, abstractmethod
from abc import ABC, abstractmethod
class CustomerDataLoader(ABC):
    @abstractmethod
    def load_data(self):
        pass