import unittest
from schedule_generation import generate_schedule, order_courses_by_section_count


class TestCourseOrdering(unittest.TestCase):
    def test_courses_ordered_by_fewest_sections_first(self):
        sections = [
            {"course": "CS120", "section": "001", "days": "MWF", "start": 900, "end": 950},
            {"course": "CS120", "section": "002", "days": "TR", "start": 900, "end": 950},
            {"course": "CS120", "section": "003", "days": "MWF", "start": 1000, "end": 1050},
            {"course": "CS121", "section": "001", "days": "TR", "start": 1100, "end": 1150},
        ]
        ordered = order_courses_by_section_count(["CS120", "CS121"], sections)
        self.assertEqual(ordered, ["CS121", "CS120"])

    def test_ordering_still_produces_valid_schedule(self):
        sections = [
            {"course": "CS120", "section": "001", "days": "MWF", "start": 900, "end": 950},
            {"course": "CS120", "section": "002", "days": "TR", "start": 930, "end": 1045},
            {"course": "CS121", "section": "001", "days": "MWF", "start": 930, "end": 1045},
        ]
        schedule = generate_schedule(["CS120", "CS121"], sections)
        self.assertIsNotNone(schedule)
        courses = {s["course"] for s in schedule}
        self.assertEqual(courses, {"CS120", "CS121"})


if __name__ == "__main__":
    unittest.main()