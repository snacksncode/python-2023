import unittest
from velo_control import *


class VeloTest(unittest.TestCase):

    def test_break(self):
        t = get_velocity_stabilize_thrust(10, 10, v_needed=0, v_current=10)
        assert t < 0

    def test_accelerate(self):
        t = get_velocity_stabilize_thrust(10, reactiveness=0.1, v_needed=10, v_current=0)
        assert t > 0

    def test_accelerate_large_maxT(self):
        t = get_velocity_stabilize_thrust(20, reactiveness=100, v_needed=10, v_current=0)
        self.assertAlmostEqual(t, 20)

    def test_landing1(self):
        t = get_velocity_stabilize_thrust(20, reactiveness=1000, v_needed=-0.1, v_current=-3.52)
        print(t)
        self.assertAlmostEqual(t, 20)



