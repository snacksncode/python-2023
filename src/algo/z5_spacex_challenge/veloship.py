from src.algo.z5_spacex_challenge.model import *
from my_helpers.velo_control import *

# veloship jest ship-em
class VeloShip(Ship):

    def initialize(self, state: ShipState):
        pass

    def get_thrust_vectors(self, time: float, state: ShipState, debug=False) -> ThrustVectors:
        h = state.height
        v = state.speed
        maxT = state.max_thrust

        plan = [DescentStep(5, -9, 1000), DescentStep(1, -1, 500), DescentStep(0.3, -0.5, 50)]

        for step in plan:
            if h > step.height:
                goal = step.target_velocity
                reactiveness = step.reactiveness
                break
        else:
            goal = -0.1
            reactiveness = 30
        thr = get_velocity_stabilize_thrust(maxT, reactiveness, goal, v)

        if debug:
            print(f'\t{thr=:6.1f},\t{goal=},\t{v=:.2f}')

        return ThrustVectors(a_vertical=thr)
