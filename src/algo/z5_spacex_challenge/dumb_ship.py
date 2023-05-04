from model import *
from my_helpers.velo_control import *

# veloship jest ship-em
class DumbShip(Ship):

    def initialize(self, state: ShipState):
        pass

    def get_thrust_vectors(self, time: float, state: ShipState, debug=False) -> ThrustVectors:
        h = state.height
        v = state.speed
        maxT = state.max_thrust

        if h > 5:
            thrust = 0
        if h > 3:
            thrust = state.max_thrust * 0.77
        else:
            thrust = 10.1

        return ThrustVectors(a_vertical=thrust)
