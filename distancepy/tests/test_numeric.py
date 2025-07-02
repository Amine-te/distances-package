"""Test numeric distance implementations."""

import pytest
import numpy as np
from distancepy.metrics.numeric import euclidean


def test_euclidean_basic():
    """Test basic Euclidean distance calculation."""
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    result = euclidean._compute(x, y)
    expected = np.sqrt(27)  # sqrt(3^2 + 3^2 + 3^2)
    assert abs(result - expected) < 1e-10


def test_euclidean_same_point():
    """Test Euclidean distance of same point."""
    x = np.array([1, 2, 3])
    result = euclidean._compute(x, x)
    assert abs(result - 0.0) < 1e-10

