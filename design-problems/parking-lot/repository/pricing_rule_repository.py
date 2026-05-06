from typing import List, Optional, Dict
from domain.pricing_rule import PricingRule
from domain.vehicle import Vehicle

class PricingRuleRepository:
    def __init__(self):
        self._rules: Dict[str, PricingRule] = {}
        self._vehicle_type_to_rule: Dict[Vehicle.VehicleType, str] = {}

    def save(self, rule: PricingRule) -> PricingRule:
        self._rules[rule.pricing_id] = rule
        self._vehicle_type_to_rule[rule.slot_type] = rule.pricing_id
        print("Saving rule:", rule.slot_type, type(rule.slot_type))
        return rule

    def find_by_id(self, rule_id: str) -> Optional[PricingRule]:
        return self._rules.get(rule_id)

    def find_by_vehicle_type(self, slot_type: Vehicle.VehicleType) -> Optional[PricingRule]:
        rule_id = self._vehicle_type_to_rule.get(slot_type)
        print("Looking for:", slot_type, type(slot_type))
        print("Keys:", list(self._vehicle_type_to_rule.keys()))
        return self._rules.get(rule_id) if rule_id else None

    def find_all(self) -> List[PricingRule]:
        return list(self._rules.values())

    def update(self, rule: PricingRule):
        if rule.pricing_id in self._rules:
            self._rules[rule.pricing_id] = rule
            self._vehicle_type_to_rule[rule.slot_type] = rule.pricing_id

    def delete(self, rule_id: str):
        rule = self._rules.pop(rule_id, None)
        if rule:
            self._vehicle_type_to_rule.pop(rule.slot_type, None)

    def clear(self):
        self._rules.clear()
        self._vehicle_type_to_rule.clear()