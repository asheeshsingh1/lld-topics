import uuid
from domain.vehicle import Vehicle

class ParkingSlot:
    """
        Parking Slot Domain Model
        Represents a area designated for a particular type of Vehicle
    """

    def __init__(self, slot_type: Vehicle.VehicleType, floor_number: int):
        self.slot_id = str(uuid.uuid4())
        self.slot_type = slot_type
        self.floor_number = floor_number
        self.occupied = False

    def __str__(self):
        return f"ParkingSlot(slot_id={self.slot_id}, slot_type={self.slot_type}, floor_number={self.floor_number},occupied={self.occupied})"