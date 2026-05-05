from domain.vehicle import Vehicle
from domain.parking_slot import ParkingSlot
from domain.ticket import Ticket
from domain.floor import Floor

car = Vehicle("UP21DB2706", Vehicle.VehicleType.CAR)
floor = Floor(floor_number=1)
slot = ParkingSlot(slot_type=Vehicle.VehicleType.CAR, floor_number=1)
ticket = Ticket(slot_id=slot.slot_id,vehicle_id=car.id)


print(car)
print(floor)
print(slot)
print(ticket)