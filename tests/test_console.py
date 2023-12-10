import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_custom_prompt(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.prompt = "(custom_prompt) "
            self.console.onecmd("prompt")
            self.assertEqual(mock_stdout.getvalue().strip(), "(custom_prompt)")

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(mock_stdout.getvalue().strip(), "Bye!")

    def test_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(mock_stdout.getvalue().strip(), "Bye!")

    def test_unknown_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("unknown_command")
            self.assertIn("*** Unknown command: unknown_command", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
