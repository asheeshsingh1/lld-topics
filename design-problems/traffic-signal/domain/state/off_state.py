from domain.state.traffic_light_state import TrafficLightState

class OffState(TrafficLightState):
    def turn_green(self, traffic_light):
        from .green_state import GreenState
        traffic_light.set_state(GreenState())
        print(f"Traffic light {traffic_light.direction} changed from OFF to GREEN")

    def turn_yellow(self, traffic_light):
        from .yellow_state import YellowState
        traffic_light.set_state(YellowState())
        print(f"Traffic light {traffic_light.direction} changed from OFF to YELLOW")

    def turn_red(self, traffic_light):
        from .red_state import RedState
        traffic_light.set_state(RedState())
        print(f"Traffic light {traffic_light.direction} changed from OFF to RED")

    def turn_off(self, traffic_light):
        print(f"Traffic light {traffic_light.direction} is already OFF")

    def get_state_name(self) -> str:
        return "OFF"

    def can_transition_to(self, new_state) -> bool:
        return True
