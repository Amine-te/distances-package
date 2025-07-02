"""
Example usage of DistancePy package
"""

import numpy as np
from distancepy import euclidean_distance

# Example 1: Point to point
print("Point to point:")
distance = euclidean_distance([0, 0], [3, 4])
print(f"Distance: {distance}")

# Example 2: Point to array
print("\nPoint to array:")
point = [0, 0]
points_array = [[1, 1], [3, 4], [6, 8]]
distances = euclidean_distance(point, points_array)
print(f"Distances: {distances}")

# Example 3: Pairwise distances
print("\nPairwise distances:")
points = [[0, 0], [3, 4], [6, 8]]
pairwise = euclidean_distance(points)
print(f"Pairwise matrix:\n{pairwise}")

# Example 4: Array to array (element-wise)
print("\nArray to array (element-wise):")
arr1 = [[1, 2], [3, 4]]
arr2 = [[5, 6], [7, 8]]
elementwise = euclidean_distance(arr1, arr2)
print(f"Element-wise distances: {elementwise}")

# Example 5: Column-wise distances
print("\nColumn-wise distances:")
matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
column_distances = euclidean_distance(matrix, axis=1)  # Between columns
print(f"Column distances:\n{column_distances}")