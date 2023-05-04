from dataclasses import dataclass


def sign(arg: float):
    return 1 if arg > 0 else -1


def get_velocity_stabilize_thrust(max_thrust: float, reactiveness: float,
                                  v_needed: float, v_current: float) -> float:
    thrust = - reactiveness * (v_current - v_needed)
    if abs(thrust) > max_thrust:
        thrust = sign(thrust) * max_thrust
    return thrust


@dataclass
class DescentStep:
    height: float
    target_velocity: float
    reactiveness: float
