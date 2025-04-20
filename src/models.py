from typing import List, Tuple

Waypoint = Tuple[float, float, float, float]  # (x, y, z, time)

class DroneMission:
    def __init__(self, drone_id: str, waypoints: List[Waypoint], start_time: float, end_time: float):
        self.drone_id = drone_id
        self.waypoints = waypoints
        self.start_time = start_time
        self.end_time = end_time
