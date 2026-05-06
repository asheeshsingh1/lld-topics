from domain.receipt import PaymentReceipt
from domain.ticket import Ticket

class ReceiptService:
    def __init__(self):
        print("[SERVICE] ReceiptService initialized")

    def generate_receipt(self, ticket: Ticket, fee: float) -> PaymentReceipt:
        return PaymentReceipt(ticket.ticket_id, fee)

    def mark_receipt_as_paid(self, receipt: PaymentReceipt):
        receipt.mark_paid()

    def generate_receipt_text(self, receipt: PaymentReceipt, ticket: Ticket) -> str:
        return (
            "📄 Receipt:\n"
            "=== PARKING RECEIPT ===\n"
            f"Receipt ID: {receipt.receipt_id}\n"
            f"Ticket ID: {ticket.ticket_id}\n"
            f"Entry Time: {ticket.entry_time}\n"
            f"Exit Time: {receipt.exit_time}\n"
            f"Total Fee: ${receipt.total_fee:.2f}\n"
            f"Payment Status: {receipt.payment_status.value}\n"
            "=====================\n"
        )