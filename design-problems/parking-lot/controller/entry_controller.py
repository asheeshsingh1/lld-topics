from service.ticket_service import TicketService
from service.slot_service import SlotService
from domain.vehicle import Vehicle
from typing import Optional, NamedTuple

class EntryResult(NamedTuple):
    success: bool
    ticket_id: Optional[str]
    slot_id: Optional[str]
    message: str

class EntryController:

    def __init__(self, ticket_service: TicketService, slot_service: SlotService):
        self._ticket_service = ticket_service
        self._slot_service = slot_service
        print("Controller[Entry]: initialized")

    def enter_vehicle(self, license_plate: str, vehicle_type: Vehicle.VehicleType):
        print(f"Controller[Entry]: Vehicle with number: {license_plate} and of type: {vehicle_type} has entered the parking lot.")
        slot = self._slot_service.allocate_slot(vehicle_type)
        if not slot:
            return EntryResult(False, None, None, f"No available slots for {vehicle_type.value}")
        
        vehicle = Vehicle(license_plate, vehicle_type)
        ticket = self._ticket_service.generate_ticket(vehicle, slot.slot_id)
        return EntryResult(True, ticket.ticket_id, slot.slot_id, "Entry successful")