from src.models import DroneMission
from src.utils import euclidean_distance_3d, interpolate

SAFETY_RADIUS = 10.0  # meters

def detect_spatial_conflicts(missions: list[DroneMission]) -> list:
    conflicts = []
    for i, mission1 in enumerate(missions):
        for mission2 in missions[i + 1:]:
            # Check spatial conflict based on waypoints
            for wp1 in mission1.waypoints:
                for wp2 in mission2.waypoints:
                    if wp1 == wp2:  # Simple example check, adjust as needed
                        conflicts.append((mission1.drone_id, mission2.drone_id, wp1))
    return conflicts

def detect_temporal_conflicts(missions: list[DroneMission]) -> list:
    conflicts = []
    for i, mission1 in enumerate(missions):
        for mission2 in missions[i + 1:]:
            # Check if missions overlap in time
            if mission1.start_time < mission2.end_time and mission2.start_time < mission1.end_time:
                conflicts.append((mission1.drone_id, mission2.drone_id))
    return conflicts

def detect_conflicts(primary: DroneMission, others: list[DroneMission]) -> list[dict]:
    conflicts = []

    # Check each waypoint pair of primary drone
    for other in others:
        for i in range(len(primary.waypoints) - 1):
            p1, t1 = primary.waypoints[i][:3], primary.waypoints[i][3]
            p2, t2 = primary.waypoints[i+1][:3], primary.waypoints[i+1][3]

            # Check each waypoint pair of the other drone
            for j in range(len(other.waypoints) - 1):
                q1, q_t1 = other.waypoints[j][:3], other.waypoints[j][3]
                q2, q_t2 = other.waypoints[j+1][:3], other.waypoints[j+1][3]

                # Check if there is a temporal overlap
                overlap_start = max(t1, q_t1)
                overlap_end = min(t2, q_t2)

                if overlap_start < overlap_end:
                    step = 1  # Small time step for interpolation
                    t = overlap_start
                    while t <= overlap_end:
                        # Interpolate positions for both drones at time t
                        primary_pos = interpolate(p1, p2, t1, t2, t)
                        other_pos = interpolate(q1, q2, q_t1, q_t2, t)
                        
                        # Calculate the Euclidean distance between the two drones
                        if euclidean_distance_3d(primary_pos, other_pos) < SAFETY_RADIUS:
                            conflicts.append({
                                'conflict_time': t,
                                'primary_pos': primary_pos,
                                'other_pos': other_pos,
                                'other_drone': other.drone_id
                            })
                            break  # Exit the loop if a conflict is detected
                        t += step  # Increment the time step
    return conflicts
