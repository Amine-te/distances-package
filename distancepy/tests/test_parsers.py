"""Test input parsers."""

import pytest
import numpy as np
import tempfile
from pathlib import Path
from distancepy.core.parsers import DataParser


def test_parse_list():
    """Test parsing list input."""
    data = [1, 2, 3, 4]
    result = DataParser.parse_single_input(data)
    expected = np.array([1, 2, 3, 4])
    np.testing.assert_array_equal(result, expected)


def test_parse_csv():
    """Test parsing CSV file."""
    # Create temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("1,2,3\n4,5,6\n7,8,9\n")
        temp_path = f.name
    
    try:
        result = DataParser.parse_single_input(temp_path)
        expected = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        np.testing.assert_array_equal(result, expected)
    finally:
        Path(temp_path).unlink()


def test_parse_csv_with_header():
    """Test parsing CSV file with header."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("x,y,z\n1,2,3\n4,5,6\n")
        temp_path = f.name
    
    try:
        result = DataParser.parse_single_input(temp_path)
        expected = np.array([[1, 2, 3], [4, 5, 6]])
        np.testing.assert_array_equal(result, expected)
    finally:
        Path(temp_path).unlink()