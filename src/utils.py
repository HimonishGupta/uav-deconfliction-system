from typing import Tuple

# Function to calculate Euclidean distance in 3D space
def euclidean_distance_3d(p1: Tuple[float, float, float], p2: Tuple[float, float, float]) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5

# Function to interpolate between two 3D points at a given time t
def interpolate(p1: Tuple[float, float, float], p2: Tuple[float, float, float], t1: float, t2: float, t: float) -> Tuple[float, float, float]:
    if t2 == t1:
        return p1  # Avoid division by zero, return p1 when t1 == t2
    alpha = (t - t1) / (t2 - t1)  # Time ratio
    return (p1[0] + alpha * (p2[0] - p1[0]),
            p1[1] + alpha * (p2[1] - p1[1]),
            p1[2] + alpha * (p2[2] - p1[2]))
