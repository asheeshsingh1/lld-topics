import uuid
from domain.vehicle import Vehicle

class PricingRule:
    """
        Pricing Rule domain Model
        Represents Dynamic Pricing based on vehicle/slot type.
    """

    def __init__(
        self,
        slot_type: Vehicle.VehicleType,
        flat_rate: float,
        hourly_rate: float
    ):
        self.pricing_id = str(uuid.uuid4())
        self.slot_type = slot_type
        self.flat_rate = flat_rate
        self.hourly_rate = hourly_rate

    def update_rate(self,hourly_rate: float, flat_rate: float):
        self.flat_rate = flat_rate
        self.hourly_rate = hourly_rate

    def __str__(self):
        return f"PricingRule(pricing_id={self.pricing_id}, flat_rate={self.flat_rate}, hourly_rate={self.hourly_rate}, slot_type={self.slot_type})"