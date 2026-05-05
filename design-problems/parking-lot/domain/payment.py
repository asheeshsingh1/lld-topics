import uuid
from enum import Enum
from adapter.pg_adapter import PaymentGatewayAdapter

class Payment:
    """
        Payment domain Model
        Represents Payment made against a parking ticket
    """

    class PaymentStatus(Enum):
        PENDING = "PENDING"
        SUCCESS = "SUCCESS"
        FAILED = "FAILED"

    def __init__(self, amount: float, ticket_id: str, payment_gateway: PaymentGatewayAdapter):
        self.payment_id = str(uuid.uuid4())
        self.ticket_id = ticket_id
        self.amount = amount
        self.gateway = payment_gateway
        self.status = self.PaymentStatus.PENDING
    
    def mark_success(self):
        self.status = self.PaymentStatus.SUCCESS

    def mark_failed(self):
        self.status = self.PaymentStatus.FAILED

    def __str__(self):
        return f"Payment(payment_id={self.payment_id}, ticket_id={self.ticket_id}, amount={self.amount}, gateway={self.gateway}, status={self.status})"