import io
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_quit_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(mock_stdout.getvalue().strip(), "Bye!")

    def test_EOF_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(mock_stdout.getvalue().strip(), "Bye!")

    def test_emptyline_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("\n"))
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith(""))

    def test_show_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel 1234-1234-1234")
            self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    def test_destroy_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel 1234-1234-1234")
            self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    def test_all_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all BaseModel")
            self.assertTrue(mock_stdout.getvalue().strip().startswith("["))

    def test_update_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel 1234-1234-1234 name 'new_name'")
            self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    def test_update_command_with_integer_attribute(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel 1234-1234-1234 age 25")
            self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    def test_update_command_with_float_attribute(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel 1234-1234-1234 price 99.99")
            self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    def test_update_command_with_list_attribute(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel 1234-1234-1234 tags ['tag1', 'tag2']")
            self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

 




if __name__ == "__main__":
    unittest.main()
