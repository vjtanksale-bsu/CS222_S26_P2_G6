import unittest
import os

from course_data import read_course_data


class TestCourseData(unittest.TestCase):

    def setUp(self):
        self.filename = "test_courses.txt"

        with open(self.filename, "w") as file:
            file.write("CS120 001 MWF 0900 0950\n")
            file.write("CS120 002 TR 1100 1215\n")
            file.write("CS121 001 MWF 1000 1050\n")

    def tearDown(self):
        os.remove(self.filename)

    def test_read_course_data(self):
        courses = read_course_data(self.filename)

        self.assertEqual(len(courses), 3)
        self.assertEqual(courses[0]["course"], "CS120")
        self.assertEqual(courses[0]["section"], "001")
        self.assertEqual(courses[0]["days"], "MWF")
        self.assertEqual(courses[0]["start"], 900)
        self.assertEqual(courses[0]["end"], 950)