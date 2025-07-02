"""
Test script to verify DistancePy works with actual CSV files.
Run create_test_data.py first to generate the test files.
"""

import numpy as np
from pathlib import Path
from distancepy import euclidean_distance

def test_file_operations():
    """Test various file operations with the generated CSV files."""
    
    test_dir = Path("test_data")
    
    if not test_dir.exists():
        print("Test data directory not found. Run create_test_data.py first!")
        return
    
    print("Testing DistancePy with CSV files...")
    print("=" * 50)
    
    # Test 1: Point to file
    print("\n1. Point to file distance:")
    try:
        origin = [0, 0]
        distances = euclidean_distance(origin, test_dir / "points_with_header.csv")
        print(f"   Origin {origin} to points in file:")
        print(f"   Distances: {distances}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: File pairwise distances
    print("\n2. Pairwise distances from file:")
    try:
        pairwise = euclidean_distance(test_dir / "points_with_header.csv")
        print(f"   Pairwise distance matrix shape: {pairwise.shape}")
        print(f"   Matrix:\n{pairwise}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 3: File to file (same dimensions)
    print("\n3. File to file distances:")
    try:
        # Create two compatible files for this test
        file1_distances = euclidean_distance(test_dir / "points_with_header.csv", 
                                           test_dir / "points_no_header.csv")
        print(f"   File-to-file element-wise distances: {file1_distances}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 4: 3D points
    print("\n4. 3D points from file:")
    try:
        distances_3d = euclidean_distance([0, 0, 0], test_dir / "points_3d.csv")
        print(f"   Origin to 3D points: {distances_3d}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 5: Matrix column-wise distances
    print("\n5. Column-wise distances from matrix file:")
    try:
        col_distances = euclidean_distance(test_dir / "matrix_data.csv", axis=1)
        print(f"   Column-wise distance matrix shape: {col_distances.shape}")
        print(f"   First few rows:\n{col_distances[:3, :3]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 6: Excel file
    print("\n6. Excel file support:")
    try:
        excel_distances = euclidean_distance([0, 0, 0], test_dir / "excel_data.xlsx")
        print(f"   Distances from Excel file: {excel_distances}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 7: Mixed data (should extract numeric columns)
    print("\n7. Mixed data handling:")
    try:
        mixed_distances = euclidean_distance([0, 0], test_dir / "mixed_data.csv")
        print(f"   Distances from mixed data: {mixed_distances}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 8: Tab-separated text file
    print("\n8. Tab-separated text file:")
    try:
        tab_distances = euclidean_distance([0, 0, 0], test_dir / "tab_separated.txt")
        print(f"   Text file distances: {tab_distances}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "=" * 50)
    print("File testing completed!")


def performance_test():
    """Test performance with larger dataset."""
    test_dir = Path("test_data")
    large_file = test_dir / "large_dataset.csv"
    
    if not large_file.exists():
        print("Large dataset not found. Run create_test_data.py first!")
        return
    
    print("\nPerformance test with 1000 points:")
    print("-" * 30)
    
    import time
    
    # Test pairwise distances on large dataset
    start_time = time.time()
    try:
        pairwise_large = euclidean_distance(large_file)
        end_time = time.time()
        
        print(f"Pairwise distances computed: {pairwise_large.shape}")
        print(f"Time taken: {end_time - start_time:.3f} seconds")
        print(f"Number of distance calculations: {pairwise_large.shape[0] * (pairwise_large.shape[0] - 1) // 2}")
    except Exception as e:
        print(f"Error in performance test: {e}")


if __name__ == "__main__":
    test_file_operations()
    performance_test()