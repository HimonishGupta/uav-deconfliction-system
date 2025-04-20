from src.models import DroneMission
from src.conflict_checker import detect_conflicts

# Load drone missions from a JSON file
def load_missions_from_json(filename: str) -> list[DroneMission]:
    import json
    with open(filename, 'r') as file:
        data = json.load(file)
        missions = []
        for mission_data in data:
            drone_id = mission_data['drone_id']
            waypoints = [(wp[0], wp[1], wp[2], wp[3]) for wp in mission_data['waypoints']]
            start_time = mission_data['start_time']
            end_time = mission_data['end_time']
            missions.append(DroneMission(drone_id, waypoints, start_time, end_time))
        return missions

# Check if there are conflicts for the primary drone mission
def check_for_conflicts(primary_mission: DroneMission, other_missions: list[DroneMission]) -> dict:
    conflicts = detect_conflicts(primary_mission, other_missions)
    if conflicts:
        return {
            'status': 'conflict detected',
            'details': conflicts
        }
    return {
        'status': 'clear',
        'details': []
    }
