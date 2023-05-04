from random import random, seed
from sim import Simulator, WindConditions
from dumb_ship import DumbShip
from veloship import VeloShip
from model import ShipState, SimulationResult, FinalState
import numpy as np

MAX_THRUST = 20

seed(111)


def run(n=50, wind_avg=0, wind_std=0.1, text='RUN', debug=False):
    total_ok = 0
    fuels = []
    for _ in range(n):
        sim = Simulator(DumbShip())
        result = sim.run_simulation(ShipState(height=10 + 2 * random(), speed=0, max_thrust=MAX_THRUST),
                                    wind=WindConditions(wind_avg, wind_std), debug=False)
        if debug:
            print(f'result: {result.status}\tfuel_used:{result.fuel_used:.0f}')
        if result.status == FinalState.OK:
            total_ok += 1
        fuels.append(result.fuel_used)

    print(f'{text} FINAL RESULT\n\tok landings: {total_ok / n * 100:.0f}%'
          f'\n\tfuel used (.95 percentile): {np.percentile(fuels, 0.95):.0f}')



if __name__ == '__main__':
    run(n=100, text='NO WIND', wind_avg=0, wind_std=0.001)
    run(n=100, text='CONSTANT WIND DOWN', wind_avg=-1, wind_std=0.001)
    run(n=100, text='VARIABLE WIND DOWN', wind_avg=-1, wind_std=1)
    run(n=100, text='TURBULENT WIND', wind_avg=0, wind_std=50)
