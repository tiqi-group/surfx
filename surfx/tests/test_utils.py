import unittest

import numpy as np
from numpy import testing as nptest

from surfx.expressions import polygon_potential  # TODO: Deleteme
from surfx.utils import expand_tensor


class BasicFunctionsCase(unittest.TestCase):
    def test_expand_tensor(self):
        a = np.array([1, 2, 3.0])[None, :]
        nptest.assert_equal(expand_tensor(a), a)
        b = np.array([1, 2, 3, 4, 5])[None, :]
        b1 = np.array(
            [1, 2, 3, 2, 4, 5, 3, 5, -5]  # triu
        ).reshape((1, 3, 3))
        nptest.assert_equal(expand_tensor(b), b1)
        c = np.random.random(5)
        ti, tj = np.triu_indices(3)
        ce = expand_tensor(c[None, :])[0, ti, tj]
        nptest.assert_equal(ce[:5], c)
        nptest.assert_equal(ce[5], -c[0] - c[3])

    def test_polygon_value(self):
        p = np.array([[1.0, 0], [2, 3], [2, 7], [3, 8], [-2, 8], [-5, 2]])
        x = np.array([[1, 2, 3.0]])
        nptest.assert_almost_equal(polygon_potential(x, [p], 1, 0, 0, 0, None), [[0.24907]])

    def test_polygon_value_grad(self):
        p = np.array([[1.0, 0], [2, 3], [2, 7], [3, 8], [-2, 8], [-5, 2]])
        x = np.array([[1, 2, 3.0]])
        nptest.assert_almost_equal(
            polygon_potential(x, [p], 1, 1, 0, 0, None),
            [[-0.0485227, 0.0404789, -0.076643]],
        )


if __name__ == "__main__":
    unittest.main()
