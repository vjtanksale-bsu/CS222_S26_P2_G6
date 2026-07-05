import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os


class TestMainIntegration(unittest.TestCase):
    def setUp(self):
        self.filename = "test_courses_integration.txt"
        with open(self.filename, "w") as f:
            f.write("CS120 001 MWF 0900 0950\n")
            f.write("CS120 002 TR 0930 1045\n")
            f.write("CS121 001 MWF 0930 1045\n")

    def tearDown(self):
        os.remove(self.filename)

    def test_full_flow_produces_valid_schedule(self):
        inputs = iter(["2", "CS120", "CS121"])
        with patch("builtins.input", lambda prompt="": next(inputs)):
            captured = StringIO()
            sys.stdout = captured
            import main
            main.run(self.filename)
            sys.stdout = sys.__stdout__

        output = captured.getvalue()
        self.assertIn("Final Course Schedule", output)
        self.assertIn("CS120", output)
        self.assertIn("CS121", output)


if __name__ == "__main__":
    unittest.main()