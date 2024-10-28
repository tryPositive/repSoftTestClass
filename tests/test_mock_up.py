import unittest
from unittest.mock import patch, mock_open
from src.mock_up import (
    read_data_from_file,
    execute_command,
    perform_action_based_on_time,
)


class TestMockUp(unittest.TestCase):

    # 1
    @patch("builtins.open", new_callable=mock_open, read_data="file content")
    def test_read_data_from_file(self, mock_open_file):
        result = read_data_from_file("test_file.txt")
        self.assertEqual(result, "file content")
        mock_open_file.assert_called_once_with("test_file.txt", "r")

    # 2
    @patch("subprocess.run")
    def test_execute_command(self, mock_run):
        mock_run.return_value.stdout = "command output"
        result = execute_command(["echo", "hello"])
        self.assertEqual(result, "command output")
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, text=True
        )

    # 3
    @patch("time.time", return_value=5)
    def test_perform_action_based_on_time_a(self, mock_time):
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("time.time", return_value=15)
    def test_perform_action_based_on_time_b(self, mock_time):
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")


if __name__ == "__main__":
    unittest.main()
