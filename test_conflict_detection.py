import unittest
from conflict_detection import has_conflict


class TestConflictDetection(unittest.TestCase):

    def test_same_days_overlapping_times_conflict(self):
        section1 = {"days": "MWF", "start": 900, "end": 950}
        section2 = {"days": "MWF", "start": 930, "end": 1020}
        self.assertTrue(has_conflict(section1, section2))

    def test_different_days_no_conflict(self):
        section1 = {"days": "MWF", "start": 900, "end": 950}
        section2 = {"days": "TR", "start": 900, "end": 950}
        self.assertFalse(has_conflict(section1, section2))

    def test_same_days_non_overlapping_times_no_conflict(self):
        section1 = {"days": "MWF", "start": 900, "end": 950}
        section2 = {"days": "MWF", "start": 1000, "end": 1050}
        self.assertFalse(has_conflict(section1, section2))

    def test_partial_day_overlap_with_time_overlap_conflict(self):
        section1 = {"days": "MWF", "start": 1300, "end": 1350}
        section2 = {"days": "MW", "start": 1300, "end": 1350}
        self.assertTrue(has_conflict(section1, section2))

    def test_adjacent_times_no_conflict(self):
        section1 = {"days": "TR", "start": 900, "end": 1015}
        section2 = {"days": "TR", "start": 1015, "end": 1130}
        self.assertFalse(has_conflict(section1, section2))

    def test_one_section_inside_another_conflict(self):
        section1 = {"days": "MWF", "start": 900, "end": 1000}
        section2 = {"days": "MWF", "start": 920, "end": 950}
        self.assertTrue(has_conflict(section1, section2))


if __name__ == "__main__":
    unittest.main()