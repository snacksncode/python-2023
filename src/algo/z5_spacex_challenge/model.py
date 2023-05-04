from dataclasses import dataclass
from enum import Enum


@dataclass
class ShipState:
    height: float
    speed: float
    max_thrust: float  # can't exceed this value in ThrustVectors


@dataclass
class ThrustVectors:
    a_vertical: float


class FinalState(Enum):
    OK = 0
    DISASSEMBLY = 1
    ILLEGAL_THRUST_VALUE = 2
    NO_LANDING = 3


@dataclass
class SimulationResult:
    fuel_used: float
    status: FinalState


class Ship:

    def __init__(self, fuel: float = 100):
        # konstruktor
        self.fuel = fuel

    def initialize(self, state: ShipState):
        # todo:  you might save the initial state
        pass

    def get_thrust_vectors(self, time: float, state: ShipState) -> ThrustVectors:
        # print(f'current fuel level: {self.fuel}')
        # todo: place for your work....
        return ThrustVectors(a_vertical=0)
