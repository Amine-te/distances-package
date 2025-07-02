"""Input validation utilities."""

import numpy as np
from pathlib import Path
from .exceptions import InputError, DimensionMismatchError


def validate_numeric_array(arr, name="array"):
    """Validate that array contains only numeric values."""
    if not isinstance(arr, np.ndarray):
        arr = np.array(arr)
    
    if arr.size == 0:
        raise InputError(f"{name} cannot be empty")
    
    if not np.issubdtype(arr.dtype, np.number):
        # Try to convert to numeric
        try:
            arr = arr.astype(float)
        except (ValueError, TypeError):
            raise InputError(f"{name} must contain only numeric values")
    
    if np.any(np.isnan(arr)) or np.any(np.isinf(arr)):
        raise InputError(f"{name} contains NaN or infinite values")
    
    return arr


def validate_dimensions(x, y):
    """Validate that two arrays have compatible dimensions."""
    x, y = np.asarray(x), np.asarray(y)
    
    if x.shape != y.shape:
        raise DimensionMismatchError(
            f"Arrays must have the same shape. Got {x.shape} and {y.shape}"
        )
    
    return x, y


def validate_file_path(path):
    """Validate file path exists and has supported extension."""
    path = Path(path)
    
    if not path.exists():
        raise InputError(f"File not found: {path}")
    
    if not path.is_file():
        raise InputError(f"Path is not a file: {path}")
    
    supported_extensions = {'.csv', '.xlsx', '.xls', '.txt'}
    if path.suffix.lower() not in supported_extensions:
        raise InputError(
            f"Unsupported file format: {path.suffix}. "
            f"Supported formats: {', '.join(supported_extensions)}"
        )
    
    return path