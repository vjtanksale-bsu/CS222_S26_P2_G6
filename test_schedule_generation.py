import unittest
from schedule_generation import generate_schedule

class TestScheduleGeneration(unittest.TestCase):
    def setUp(self):
        self.all_sections = [
            {"course": "CS120", "section": "001", "days": "MWF", "start": 900, "end": 950},
            {"course": "CS120", "section": "002", "days": "TR",  "start": 930, "end": 1045},
            {"course": "CS121", "section": "001", "days": "MWF", "start": 930, "end": 1045},
            {"course": "CS121", "section": "002", "days": "TR",  "start": 1100, "end": 1215}
        ]

    def test_generate_valid_schedule_success(self):
        selected = ["CS120", "CS121"]
        schedule = generate_schedule(selected, self.all_sections)
        self.assertIsNotNone(schedule)
        self.assertEqual(len(schedule), 2)
        courses_in_schedule = [s["course"] for s in schedule]
        self.assertIn("CS120", courses_in_schedule)
        self.assertIn("CS121", courses_in_schedule)

    def test_no_valid_schedule_exists(self):
        selected = ["CS120", "CS121"]
        bad_sections = [
            {"course": "CS120", "section": "001", "days": "MWF", "start": 900, "end": 950},
            {"course": "CS121", "section": "001", "days": "MWF", "start": 930, "end": 1045}
        ]
        schedule = generate_schedule(selected, bad_sections)
        self.assertIsNone(schedule)

    def test_complex_backtracking_path(self):
        selected = ["CS120", "CS121", "CS222"]
        complex_sections = [
            {"course": "CS120", "section": "001", "days": "M", "start": 900, "end": 1000},
            {"course": "CS121", "section": "001", "days": "M", "start": 930, "end": 1030},
            {"course": "CS121", "section": "002", "days": "W", "start": 900, "end": 1000},
            {"course": "CS222", "section": "001", "days": "W", "start": 930, "end": 1030},
            {"course": "CS222", "section": "002", "days": "F", "start": 900, "end": 1000}
        ]
        schedule = generate_schedule(selected, complex_sections)
        self.assertIsNotNone(schedule)
        self.assertEqual(len(schedule), 3)
        
        sections_picked = {s["course"]: s["section"] for s in schedule}
        self.assertEqual(sections_picked["CS120"], "001")
        self.assertEqual(sections_picked["CS121"], "002")
        self.assertEqual(sections_picked["CS222"], "002")

if __name__ == "__main__":
    unittest.main()
