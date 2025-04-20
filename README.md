# UAV Deconfliction System

A Python-based simulation tool to detect and visualize spatial and temporal conflicts between a primary drone mission and other scheduled UAV flights. Built for airspace safety and mission planning in multi-drone environments.

## Overview
This system checks whether a drone's planned waypoint mission is conflict-free by comparing it with other drones in shared airspace, considering both spatial and temporal overlaps.

## Features
- **Spatial & Temporal Deconfliction**: Detect conflicts based on drone positions and flight times.
- **Conflict Explanation**: Provides detailed information on the detected conflict (if any).
- **3D Visualization**: Visualizes the drone flights and potential conflicts in 3D space.
- **Modular Python Codebase**: Easily extendable for integration with other UAV systems or further customization.
- **Simulation Results**: Generates conflict-free and conflict-present scenarios for analysis.

## Results

Conflict-free scenario visualization: ![Screenshot 2025-04-20 132358](https://github.com/user-attachments/assets/f3266d2d-d314-4c19-afec-354099fd5a56)


Conflict-present scenario visualization:![Screenshot 2025-04-20 132437](https://github.com/user-attachments/assets/29f13e47-d88e-4fac-a308-b70e72984b48)


## Setup
To install dependencies, run the following command:

```bash
pip install matplotlib

