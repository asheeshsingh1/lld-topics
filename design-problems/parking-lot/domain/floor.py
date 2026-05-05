import uuid
from typing import List
from domain.vehicle import Vehicle
from domain.parking_slot import ParkingSlot

class Floor:
    """
        Floor Domain Model
        Represents a single floor in a parking lot.
    """

    def __init__(self, floor_number: int):
        self.floor_id = str(uuid.uuid4())
        self.floor_number = floor_number
        self.slots: List[ParkingSlot] = []

    def add_slot(self, slot: ParkingSlot):
        if slot in self.slots:
            raise ValueError("Slot already exists on this floor")
        self.slots.append(slot)

    def get_available_slots(self, slot_type: Vehicle.VehicleType) -> List[ParkingSlot]:
        return [s for s in self.slots if s.slot_type == slot_type and not s.occupied]
    
    def get_available_slots_count(self, slot_type: Vehicle.VehicleType) -> int:
        return len(self.get_available_slots(slot_type))
    
    def __str__(self):
        return f"Floor(floor_id={self.floor_id},floor_number={self.floor_number},total_slots={len(self.slots)})"