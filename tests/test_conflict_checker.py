import unittest
from src.utils import euclidean_distance_3d
from src.conflict_checker import detect_conflicts
from src.models import DroneMission

class TestConflictChecker(unittest.TestCase):
    def test_euclidean_distance(self):
        p1 = (0, 0, 0)
        p2 = (3, 4, 0)
        self.assertEqual(euclidean_distance_3d(p1, p2), 5)

    def test_detect_conflicts(self):
        mission1 = DroneMission("drone1", [(0, 0, 0, 0), (10, 10, 10, 5)], 0, 10)
        mission2 = DroneMission("drone2", [(5, 5, 5, 2), (15, 15, 15, 7)], 2, 7)
        conflicts = detect_conflicts(mission1, [mission2])
        self.assertGreater(len(conflicts), 0)

if __name__ == "__main__":
    unittest.main()
