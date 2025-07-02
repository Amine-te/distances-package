"""Input parsing utilities for different data formats."""

import numpy as np
import pandas as pd
from pathlib import Path
from typing import Union, List, Tuple, Any
from .exceptions import ParsingError, FileFormatError
from .validators import validate_file_path, validate_numeric_array


class DataParser:
    """Handles parsing of various input formats into numpy arrays."""
    
    @staticmethod
    def parse_single_input(data: Any) -> np.ndarray:
        """Parse a single input into a numpy array."""
        if isinstance(data, (str, Path)):
            return DataParser._parse_file(data)
        elif isinstance(data, (list, tuple)):
            return validate_numeric_array(np.array(data))
        elif isinstance(data, np.ndarray):
            return validate_numeric_array(data)
        elif isinstance(data, (int, float)):
            return validate_numeric_array(np.array([data]))
        else:
            raise ParsingError(f"Unsupported input type: {type(data)}")
    
    @staticmethod
    def _parse_file(file_path: Union[str, Path]) -> np.ndarray:
        """Parse file into numpy array."""
        path = validate_file_path(file_path)
        
        try:
            if path.suffix.lower() == '.csv':
                return DataParser._parse_csv(path)
            elif path.suffix.lower() in ['.xlsx', '.xls']:
                return DataParser._parse_excel(path)
            elif path.suffix.lower() == '.txt':
                return DataParser._parse_txt(path)
        except Exception as e:
            raise FileFormatError(f"Failed to parse file {path}: {str(e)}")
    
    @staticmethod
    def _parse_csv(path: Path) -> np.ndarray:
        """Parse CSV file."""
        try:
            # Try reading without header first
            df = pd.read_csv(path, header=None)
            # Check if first row contains non-numeric data (likely header)
            if df.iloc[0].dtype == 'object' or not pd.api.types.is_numeric_dtype(df.iloc[0]):
                try:
                    # Try reading first row as strings
                    first_row = pd.read_csv(path, nrows=1).iloc[0]
                    if first_row.dtype == 'object':
                        # Likely header, skip it
                        df = pd.read_csv(path, header=0)
                except:
                    pass
            
            # Convert to numeric, coerce errors to NaN
            df = df.apply(pd.to_numeric, errors='coerce')
            
            # Drop rows/columns that are all NaN
            df = df.dropna(how='all').dropna(axis=1, how='all')
            
            if df.empty:
                raise ParsingError("No numeric data found in CSV file")
            
            return df.values
            
        except Exception as e:
            raise ParsingError(f"Failed to parse CSV: {str(e)}")
    
    @staticmethod
    def _parse_excel(path: Path) -> np.ndarray:
        """Parse Excel file."""
        try:
            df = pd.read_excel(path)
            
            # Convert to numeric, coerce errors to NaN
            df = df.apply(pd.to_numeric, errors='coerce')
            
            # Drop rows/columns that are all NaN
            df = df.dropna(how='all').dropna(axis=1, how='all')
            
            if df.empty:
                raise ParsingError("No numeric data found in Excel file")
            
            return df.values
            
        except Exception as e:
            raise ParsingError(f"Failed to parse Excel: {str(e)}")
    
    @staticmethod
    def _parse_txt(path: Path) -> np.ndarray:
        """Parse text file (assuming space/tab delimited)."""
        try:
            # Try different delimiters
            for delimiter in [None, '\t', ' ', ',']:
                try:
                    df = pd.read_csv(path, delimiter=delimiter, header=None)
                    df = df.apply(pd.to_numeric, errors='coerce')
                    df = df.dropna(how='all').dropna(axis=1, how='all')
                    
                    if not df.empty:
                        return df.values
                except:
                    continue
            
            raise ParsingError("Could not parse text file with any delimiter")
            
        except Exception as e:
            raise ParsingError(f"Failed to parse text file: {str(e)}")


class DistanceInputParser:
    """Handles parsing of inputs specifically for distance calculations."""
    
    @staticmethod
    def parse_distance_inputs(x: Any, y: Any = None, axis: int = 0) -> Tuple[np.ndarray, np.ndarray, str]:
        """
        Parse inputs for distance calculation.
        
        Returns:
            x_array, y_array, calculation_type
        """
        x_array = DataParser.parse_single_input(x)
        
        if y is None:
            # Pairwise distances within x
            return x_array, x_array, "pairwise"
        
        y_array = DataParser.parse_single_input(y)
        
        # Determine calculation type
        if x_array.shape == y_array.shape:
            if x_array.ndim == 1:
                return x_array, y_array, "point_to_point"
            else:
                return x_array, y_array, "array_to_array"
        elif x_array.ndim == 1 and y_array.ndim == 2:
            return x_array, y_array, "point_to_array"
        elif x_array.ndim == 2 and y_array.ndim == 1:
            return y_array, x_array, "point_to_array"  # Swap for consistency
        else:
            # Try to broadcast or handle different shapes
            return x_array, y_array, "mixed"