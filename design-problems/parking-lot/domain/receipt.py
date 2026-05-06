import uuid
import datetime
from enum import Enum

class PaymentReceipt:
    """
        Payment Receipt domain Model
        Represent a receipt received by customer when they exit which has payment status.
    """

    class PaymentStatus(Enum):
        SUCCESS = "SUCCESS"
        PENDING = "PENDING"
        FAILED = "FAILED"

    def __init__(self, ticket_id: str, total_fee: float):
        self.receipt_id = str(uuid.uuid4())
        self.ticket_id = ticket_id
        self.exit_time = datetime.time()
        self.total_fee = total_fee
        self.payment_status = self.PaymentStatus.PENDING

    def mark_paid(self):
        self.payment_status = self.PaymentStatus.SUCCESS
    
    def __str__(self):
        return f"Receipt(id={self.id}, ticket={self.ticket_id}, fee={self.total_fee}, status={self.payment_status.value})"