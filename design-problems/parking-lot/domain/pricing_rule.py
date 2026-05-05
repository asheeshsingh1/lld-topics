import uuid
from domain.vehicle import Vehicle

class PricingRule:
    """
        Pricing Rule domain Model
        Represents Dynamic Pricing based on vehicle/slot type.
    """

    def __init__(self, flat: float, hourly: float, slot_type: Vehicle.VehicleType):
        self.pricing_id = str(uuid.uuid4())
        self.flat_rate = flat
        self.hourly_rate = hourly
        self.slot_type = slot_type

    def update_rate(self,hourly_rate: float, flat_rate: float):
        self.flat_rate = flat_rate
        self.hourly_rate = hourly_rate

    def __str__(self):
        return f"PricingRule(pricing_id={self.pricing_id}, flat_rate={self.flat_rate}, hourly_rate={self.hourly_rate}, slot_type={self.slot_type})"