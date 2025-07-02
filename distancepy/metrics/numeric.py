"""Numeric distance metrics."""

import numpy as np
from ..core.base import NumericDistance


class EuclideanDistance(NumericDistance):
    """Euclidean distance implementation."""
    
    def __init__(self):
        super().__init__("euclidean")
    
    def _compute(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Compute Euclidean distance between two points/arrays.
        
        Formula: sqrt(sum((x_i - y_i)^2))
        """
        diff = x - y
        return np.sqrt(np.sum(diff * diff))


# Create singleton instance
euclidean = EuclideanDistance()