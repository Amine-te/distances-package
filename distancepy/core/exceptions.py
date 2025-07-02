"""Custom exceptions for DistancePy."""


class DistancePyError(Exception):
    """Base exception for DistancePy."""
    pass


class InputError(DistancePyError):
    """Raised when input data is invalid."""
    pass


class DimensionMismatchError(DistancePyError):
    """Raised when input dimensions don't match."""
    pass


class FileFormatError(DistancePyError):
    """Raised when file format is not supported or corrupted."""
    pass


class ParsingError(DistancePyError):
    """Raised when data parsing fails."""
    pass