"""Test the public API."""

import pytest
import numpy as np
from distancepy import euclidean_distance


def test_point_to_point():
    """Test point to point distance."""
    result = euclidean_distance([0, 0], [3, 4])
    assert abs(result - 5.0) < 1e-10


def test_pairwise():
    """Test pairwise distances."""
    points = [[0, 0], [3, 4], [6, 8]]
    result = euclidean_distance(points)
    expected = np.array([
        [0, 5, 10],
        [5, 0, 5],
        [10, 5, 0]
    ])
    np.testing.assert_array_almost_equal(result, expected)


def test_point_to_array():
    """Test point to array distances."""
    point = [0, 0]
    array = [[3, 4], [6, 8], [0, 0]]
    result = euclidean_distance(point, array)
    expected = np.array([5, 10, 0])
    np.testing.assert_array_almost_equal(result, expected)

