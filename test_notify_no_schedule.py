import unittest
import sys
from io import StringIO
from notify_no_schedule import notify_no_schedule


class TestNotifyNoSchedule(unittest.TestCase):
    def test_notify_message_displayed(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        notify_no_schedule()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("No conflict-free schedule could be found", output)
        self.assertIn("selected courses", output)


if __name__ == "__main__":
    unittest.main()