"""Public API interface for DistancePy."""

from ..metrics import euclidean


def euclidean_distance(x, y=None, axis=0):
    """
    Calculate Euclidean distance with flexible input support.
    
    Args:
        x: First input (number, list, array, or file path)
        y: Second input (number, list, array, or file path). If None, compute pairwise distances.
        axis: Axis along which to compute distances (0=rows, 1=columns)
    
    Returns:
        float or numpy.ndarray: Distance(s)
    
    Examples:
        # Point to point
        >>> euclidean_distance([1, 2], [4, 6])
        5.0
        
        # Point to array (file)
        >>> euclidean_distance([0, 0], "data.csv")
        array([...])
        
        # Array to array
        >>> euclidean_distance([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        array([5.656854, 5.656854])
        
        # Pairwise distances
        >>> euclidean_distance([[1, 2], [3, 4], [5, 6]])
        array([[0, 2.828427, 5.656854],
               [2.828427, 0, 2.828427],
               [5.656854, 2.828427, 0]])
    """
    return euclidean(x, y, axis)