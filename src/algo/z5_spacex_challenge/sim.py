from copy import copy
from dataclasses import dataclass


@dataclass
class ShipState:
    height: float
    speed: float


@dataclass
class ThrustVectors:
    a_vertical: float


class Ship:

    def initialize(self, state: ShipState):
        pass

    def get_thrust_vectors(self, time: float, state: ShipState) -> ThrustVectors:
        # todo: place for your work....
        h = state.height
        v = state.speed
        thr = 0
        if v < -2:
            # za szybko w dół
            thr = 5
        if v > 2:
            thr = -5

        if h < 2:
            thr = 4.5 / (h+1)

        return ThrustVectors(a_vertical=thr)


class Simulator:

    def __init__(self, ship: Ship):
        self.ship = ship
        self.dt = 0.001
        self.g = -10

    def run_simulation(self, start_conditions: ShipState):
        state = start_conditions
        self.ship.initialize(state)
        t = 0
        CLOCK = 0.5
        clock = CLOCK

        while t < 10:
            thrust_vectors = self.ship.get_thrust_vectors(t, copy(state))

            state.height += state.speed * self.dt
            state.speed += (self.g + thrust_vectors.a_vertical) * self.dt
            t += self.dt
            clock -= self.dt
            if clock<0:
                print(f'{t=:.3f} {state}')
                clock = CLOCK
            if state.height < -2:
                print('disassembly\n---------')
                break

        return copy(state)


if __name__ == '__main__':
    sim = Simulator(Ship())
    pos = sim.run_simulation(ShipState(height=10, speed=0))
    print('result', pos)
    print('expected height: ', 10 + sim.g * 10 ** 2 / 2)
    print(0 + sim.g * 10)
