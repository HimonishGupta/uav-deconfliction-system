from src.interface import load_missions_from_json, check_for_conflicts
from src.models import DroneMission
from src.visualizer import plot_missions_3d

# Load missions from a JSON file
missions = load_missions_from_json('data/simulated_drones.json')

# Select a primary mission (e.g., the first mission in the list)
primary_mission = missions[0]

# Get other missions for comparison
other_missions = missions[1:]

# Check for conflicts
result = check_for_conflicts(primary_mission, other_missions)

# Print result
if result['status'] == 'conflict detected':
    print("Conflicts detected!")
    for conflict in result['details']:
        print(f"At time {conflict['conflict_time']}:")
        print(f"  Primary Drone Position: {conflict['primary_pos']}")
        print(f"  Other Drone Position: {conflict['other_pos']}")
else:
    print("No conflicts detected.")

# Visualize all missions in 3D (conflicts will appear as red points)
plot_missions_3d(missions, conflicts=result['details'], title="Conflict-Present UAV Simulation")
