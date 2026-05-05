from abc import ABC, abstractmethod

class PaymentGatewayAdapter(ABC):
    
    @abstractmethod
    def pay(self, amount: float, ticket_id: str):
        pass