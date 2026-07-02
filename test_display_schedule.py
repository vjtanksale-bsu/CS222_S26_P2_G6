import unittest
import sys
from io import StringIO
from display_schedule import display_schedule

class TestDisplaySchedule(unittest.TestCase):
    def test_display_valid_schedule_format(self):
        sample_schedule = [
            {"course": "CS120", "section": "001", "days": "MWF", "start": 900, "end": 950},
            {"course": "CS121", "section": "002", "days": "TR",  "start": 1100, "end": 1215}
        ]
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        display_schedule(sample_schedule)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("CS120", output)
        self.assertIn("001", output)
        self.assertIn("MWF", output)
        self.assertIn("900", output)
        self.assertIn("950", output)
        
        self.assertIn("CS121", output)
        self.assertIn("002", output)
        self.assertIn("TR", output)
        self.assertIn("1100", output)
        self.assertIn("1215", output)

if __name__ == "__main__":
    unittest.main()