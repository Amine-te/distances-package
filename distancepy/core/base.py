"""Base classes for distance metrics."""

from abc import ABC, abstractmethod
import numpy as np
from typing import Union, Any
from .parsers import DistanceInputParser
from .validators import validate_dimensions


class BaseDistance(ABC):
    """Abstract base class for all distance metrics."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def _compute(self, x: np.ndarray, y: np.ndarray) -> Union[float, np.ndarray]:
        """Compute distance between two arrays. Must be implemented by subclasses."""
        pass
    
    def __call__(self, x: Any, y: Any = None, axis: int = 0) -> Union[float, np.ndarray]:
        """
        Calculate distance with flexible input parsing.
        
        Args:
            x: First input (point, list, array, or file)
            y: Second input (point, list, array, or file). If None, compute pairwise distances.
            axis: Axis along which to compute distances (0=rows, 1=columns)
        
        Returns:
            Distance(s) as float or numpy array
        """
        x_array, y_array, calc_type = DistanceInputParser.parse_distance_inputs(x, y, axis)
        
        if calc_type == "point_to_point":
            x_array, y_array = validate_dimensions(x_array, y_array)
            return float(self._compute(x_array, y_array))
        
        elif calc_type == "array_to_array":
            return self._compute_array_to_array(x_array, y_array, axis)
        
        elif calc_type == "point_to_array":
            return self._compute_point_to_array(x_array, y_array, axis)
        
        elif calc_type == "pairwise":
            return self._compute_pairwise(x_array, axis)
        
        else:  # mixed
            return self._compute_mixed(x_array, y_array, axis)
    
    def _compute_array_to_array(self, x: np.ndarray, y: np.ndarray, axis: int) -> np.ndarray:
        """Compute element-wise distances between two arrays."""
        if axis == 0:  # Row-wise
            return np.array([self._compute(x[i], y[i]) for i in range(x.shape[0])])
        else:  # Column-wise
            return np.array([self._compute(x[:, i], y[:, i]) for i in range(x.shape[1])])
    
    def _compute_point_to_array(self, point: np.ndarray, array: np.ndarray, axis: int) -> np.ndarray:
        """Compute distances from a point to each row/column in an array."""
        if axis == 0:  # Point to each row
            return np.array([self._compute(point, array[i]) for i in range(array.shape[0])])
        else:  # Point to each column
            return np.array([self._compute(point, array[:, i]) for i in range(array.shape[1])])
    
    def _compute_pairwise(self, array: np.ndarray, axis: int) -> np.ndarray:
        """Compute pairwise distances within an array."""
        if axis == 0:  # Between rows
            n = array.shape[0]
            distances = np.zeros((n, n))
            for i in range(n):
                for j in range(i + 1, n):
                    dist = self._compute(array[i], array[j])
                    distances[i, j] = distances[j, i] = dist
            return distances
        else:  # Between columns
            n = array.shape[1]
            distances = np.zeros((n, n))
            for i in range(n):
                for j in range(i + 1, n):
                    dist = self._compute(array[:, i], array[:, j])
                    distances[i, j] = distances[j, i] = dist
            return distances
    
    def _compute_mixed(self, x: np.ndarray, y: np.ndarray, axis: int) -> np.ndarray:
        """Handle mixed/irregular array shapes."""
        # Try to flatten and compute if possible
        try:
            x_flat = x.flatten()
            y_flat = y.flatten()
            min_len = min(len(x_flat), len(y_flat))
            return self._compute(x_flat[:min_len], y_flat[:min_len])
        except Exception:
            raise ValueError(f"Cannot compute distance between arrays of shapes {x.shape} and {y.shape}")


class NumericDistance(BaseDistance):
    """Base class for numeric distance metrics."""
    
    def __init__(self, name: str):
        super().__init__(name)