"""
Create test CSV files for DistancePy testing.
Run this script to generate sample data files.
"""

import csv
import pandas as pd
from pathlib import Path

def create_test_data():
    """Create various test CSV files for different scenarios."""
    
    # Create test data directory
    test_dir = Path("test_data")
    test_dir.mkdir(exist_ok=True)
    
    # 1. Simple points without header
    print("Creating points_no_header.csv...")
    with open(test_dir / "points_no_header.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([0, 0])
        writer.writerow([3, 4])
        writer.writerow([6, 8])
        writer.writerow([1, 1])
        writer.writerow([5, 12])
    
    # 2. Points with header
    print("Creating points_with_header.csv...")
    with open(test_dir / "points_with_header.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])
        writer.writerow([0, 0])
        writer.writerow([3, 4])
        writer.writerow([6, 8])
        writer.writerow([1, 1])
        writer.writerow([5, 12])
    
    # 3. 3D points
    print("Creating points_3d.csv...")
    with open(test_dir / "points_3d.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y', 'z'])
        writer.writerow([0, 0, 0])
        writer.writerow([1, 2, 3])
        writer.writerow([4, 5, 6])
        writer.writerow([7, 8, 9])
    
    # 4. Matrix data (for column-wise testing)
    print("Creating matrix_data.csv...")
    matrix_data = [
        [1, 4, 7, 10],
        [2, 5, 8, 11],
        [3, 6, 9, 12]
    ]
    with open(test_dir / "matrix_data.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['col1', 'col2', 'col3', 'col4'])
        for row in matrix_data:
            writer.writerow(row)
    
    # 5. Single point (for point-to-file testing)
    print("Creating single_point.csv...")
    with open(test_dir / "single_point.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([0, 0])
    
    # 6. Mixed data with some text (should handle gracefully)
    print("Creating mixed_data.csv...")
    with open(test_dir / "mixed_data.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'x', 'y', 'category'])
        writer.writerow(['point1', 1, 2, 'A'])
        writer.writerow(['point2', 3, 4, 'B'])
        writer.writerow(['point3', 5, 6, 'A'])
    
    # 7. Tab-separated file
    print("Creating tab_separated.txt...")
    with open(test_dir / "tab_separated.txt", 'w') as f:
        f.write("1\t2\t3\n")
        f.write("4\t5\t6\n")
        f.write("7\t8\t9\n")
    
    # 8. Excel file
    print("Creating excel_data.xlsx...")
    df = pd.DataFrame({
        'x': [0, 3, 6, 9],
        'y': [0, 4, 8, 12],
        'z': [1, 2, 3, 4]
    })
    df.to_excel(test_dir / "excel_data.xlsx", index=False)
    
    # 9. Large dataset for performance testing
    print("Creating large_dataset.csv...")
    import random
    with open(test_dir / "large_dataset.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])
        for _ in range(1000):
            writer.writerow([random.uniform(-100, 100), random.uniform(-100, 100)])
    
    print(f"\nTest files created in '{test_dir}' directory:")
    for file in sorted(test_dir.glob("*")):
        print(f"  - {file.name}")
    

if __name__ == "__main__":
    create_test_data()