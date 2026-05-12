import unittest

import numpy as np
from numpy import testing as nptest

from surfx.potential import electrode_potential
from surfx.utils import expand_tensor

# TODO: Need to add this once the cover is added
# class CoverCase(unittest.TestCase):
#     def setUp(self):
#         self.c = electrode.CoverElectrode(height=20)
#         self.x = np.array([[1, 2, 3.]])

#     def test_pot(self):
#         nptest.assert_almost_equal(self.c.potential(
#             self.x, 0), [[3/20.]])

#     def test_grad(self):
#         nptest.assert_almost_equal(self.c.potential(
#             self.x, 1), [[0, 0, 1/20.]])

#     def test_curve(self):
#         nptest.assert_almost_equal(self.c.potential(
#             self.x, 2).sum(), 0.)

#     def test_orientation(self):
#         nptest.assert_almost_equal(self.c.orientations(), [])


class PolygonTestCase(unittest.TestCase):
    def setUp(self):
        self.polygon = np.array([[1, 0], [2, 3], [2, 7], [3, 8], [-2, 8], [-5, 2]])
        self.x = 1
        self.y = 2
        self.z = 3
        self.positions = (self.x, self.y, self.z)
        self.cover_height = 50.0
        self.cover_nmax = 0
        self.voltage = 1.0

    def test_pot_cover(self):
        cover_positions = (0, 0, self.cover_height)

        # potential should be zero at the cover height
        nptest.assert_allclose(
            electrode_potential(
                self.polygon,
                0.0,
                *cover_positions,
                0,
                self.cover_height,
                cover_nmax=10,
            ),
            0,
            atol=1e-5,
        )

        # field should be zero in direction at the cover height
        nptest.assert_allclose(
            electrode_potential(
                self.polygon,
                0.0,
                *cover_positions,
                1,
                self.cover_height,
                cover_nmax=10,
            ),
            0,
            atol=1e-5,
        )

    def test_known_pot(self):
        nptest.assert_almost_equal(
            electrode_potential(
                self.polygon,
                self.voltage,
                *self.positions,
                0,
                self.cover_height,
                cover_nmax=self.cover_nmax,
            ),
            0.24907,
        )

    def test_known_grad(self):
        nptest.assert_almost_equal(
            electrode_potential(
                self.polygon,
                self.voltage,
                *self.positions,
                1,
                self.cover_height,
                cover_nmax=self.cover_nmax,
            ),
            expand_tensor(np.array([-0.0485227, 0.0404789, -0.076643])),
        )

    def test_known_curve(self):
        nptest.assert_almost_equal(
            electrode_potential(
                self.polygon,
                self.voltage,
                *self.positions,
                2,
                self.cover_height,
                cover_nmax=self.cover_nmax,
            ),
            expand_tensor(np.array([-0.0196946, -0.00747322, 0.0287624, -0.014943, -0.0182706])),
        )


if __name__ == "__main__":
    unittest.main()
