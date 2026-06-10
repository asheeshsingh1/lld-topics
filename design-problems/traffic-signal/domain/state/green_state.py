from domain.state.traffic_light_state import TrafficLightState
from domain.state.invalid_state_transition import InvalidStateTransitionException

class GreenState(TrafficLightState):
    def turn_green(self, traffic_light):
        print(f"Traffic light {traffic_light.direction} is already GREEN")

    def turn_yellow(self, traffic_light):
        from .yellow_state import YellowState
        traffic_light.set_state(YellowState())
        print(f"Traffic light {traffic_light.direction} changed from GREEN to YELLOW")

    def turn_red(self, traffic_light):
        raise InvalidStateTransitionException("GREEN", "RED")

    def turn_off(self, traffic_light):
        from .off_state import OffState
        traffic_light.set_state(OffState())
        print(f"Traffic light {traffic_light.direction} changed from GREEN to OFF")

    def get_state_name(self) -> str:
        return "GREEN"

    def can_transition_to(self, new_state) -> bool:
        from .yellow_state import YellowState
        from .off_state import OffState
        return isinstance(new_state, (YellowState, OffState))
