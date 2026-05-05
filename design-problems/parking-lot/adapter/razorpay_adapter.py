import random
from adapter.pg_adapter import PaymentGatewayAdapter

class RazorPayAdapter(PaymentGatewayAdapter):

    def pay(self, amount: float, ticket_id: str) -> bool:
        print(f"Using Razor Pay PG to pay amount: {amount} against ticket: {ticket_id}")
        success = random.random() < 0.9
        return success