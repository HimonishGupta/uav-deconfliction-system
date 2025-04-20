# src/visualizer.py

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_missions_3d(missions, conflicts=None, title="UAV 3D Path Simulation"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    colors = ['blue', 'green', 'purple', 'orange', 'cyan']

    for idx, mission in enumerate(missions):
        xs = [wp[0] for wp in mission.waypoints]
        ys = [wp[1] for wp in mission.waypoints]
        zs = [wp[2] for wp in mission.waypoints]
        ax.plot(xs, ys, zs, label=f"Drone {mission.drone_id}", color=colors[idx % len(colors)])
        ax.scatter(xs, ys, zs, marker='o', s=30)

    if conflicts:
        for conflict in conflicts:
            x, y, z = conflict['primary_pos']
            ax.scatter(x, y, z, color='red', s=80, label="Conflict" if "Conflict" not in ax.get_legend_handles_labels()[1] else "")

    ax.set_title(title)
    ax.set_xlabel('X (meters)')
    ax.set_ylabel('Y (meters)')
    ax.set_zlabel('Z (altitude)')
    ax.legend()
    plt.tight_layout()
    plt.show()
