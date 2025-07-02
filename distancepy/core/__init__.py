"""Core functionality for DistancePy."""

from .base import BaseDistance, NumericDistance
from .exceptions import (
    DistancePyError, 
    InputError, 
    DimensionMismatchError, 
    FileFormatError, 
    ParsingError
)
from .parsers import DataParser, DistanceInputParser
from .validators import validate_numeric_array, validate_dimensions, validate_file_path

__all__ = [
    "BaseDistance",
    "NumericDistance",
    "DistancePyError",
    "InputError",
    "DimensionMismatchError",
    "FileFormatError",
    "ParsingError",
    "DataParser",
    "DistanceInputParser",
    "validate_numeric_array",
    "validate_dimensions",
    "validate_file_path",
]