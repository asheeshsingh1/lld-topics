import uuid
from datetime import datetime

class Ticket:
    """
        Ticket Domain Model
        Represents Ticket issue for a parking slot in a parking lot.
    """

    def __init__(self, vehicle_id: str, slot_id: str):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle_id = vehicle_id
        self.slot_id = slot_id
        self.entry_time = datetime.now()
        self.active = True
    
    def deactivate(self):
        self.active = False

    def __str__(self):
        return f"Ticket(ticket_id={self.ticket_id},vehicle_id={self.vehicle_id},slot_id={self.slot_id},entry_time={self.entry_time},active={self.active})"