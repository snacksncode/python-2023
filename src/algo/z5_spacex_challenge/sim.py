from copy import copy
from model import *
from dumb_ship import DumbShip
from veloship import VeloShip
from random import gauss


class WindConditions:
    def __init__(self, average: float, deviation: float):
        self.deviation = deviation
        self.average = average

    def get_wind_speed(self):
        return gauss(self.average, self.deviation)


class Simulator:

    def __init__(self, ship: Ship, ):
        self.ship = ship
        self.dt = 0.01
        self.g = -10
        self.wind_conditions = None

    def run_simulation(self, start_conditions: ShipState, wind=WindConditions(0, 0.1), debug=True) -> SimulationResult:
        self.wind_conditions = wind

        """
        This function performs a single run of a simulation
        :param start_conditions: where the ship is before start
        :param debug: show debug information on ships position and actions during simulation
        :return: final position of the ship
        """

        state = start_conditions
        self.ship.initialize(state)
        t = 0
        CLOCK = 0.2  # for debug during simulation
        clock = CLOCK
        total_fuel_used = 0

        while t < 20:
            thrust_vectors = self.ship.get_thrust_vectors(time=t, state=copy(state))
            if thrust_vectors.a_vertical > start_conditions.max_thrust:
                return SimulationResult(fuel_used=total_fuel_used, status=FinalState.ILLEGAL_THRUST_VALUE)

            state.height += state.speed * self.dt
            state.speed += (self.g + thrust_vectors.a_vertical + 0.1 * self.wind_conditions.get_wind_speed()) * self.dt
            total_fuel_used += thrust_vectors.a_vertical

            t += self.dt
            clock -= self.dt
            if clock < 0:
                if debug:
                    print(f'{t=:.3f}\t\theight={state.height:.1f}\t'
                          f'speed={state.speed:.3f} thr={thrust_vectors.a_vertical:.1f}')
                clock = CLOCK
            if state.height < 0:
                if abs(state.speed) < 0.5:
                    return SimulationResult(total_fuel_used, FinalState.OK)
                else:
                    return SimulationResult(total_fuel_used, FinalState.DISASSEMBLY)

        return SimulationResult(total_fuel_used, FinalState.NO_LANDING)


if __name__ == '__main__':
    MAX_THRUST = 20
    # sim = Simulator(VeloShip())
    sim = Simulator(DumbShip())
    result = sim.run_simulation(ShipState(height=10, speed=0, max_thrust=MAX_THRUST))
    print(f'\nresult: {result.status}\tfuel_used:{result.fuel_used:.0f}')
