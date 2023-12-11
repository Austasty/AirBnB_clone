#!/usr/bin/python3

import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_do_quit(self):
        with self.assertRaises(SystemExit) as cm:
            self.console.onecmd("quit")
        self.assertEqual(cm.exception.code, None)

    def test_do_EOF(self):
        with self.assertRaises(SystemExit) as cm:
            self.console.onecmd("EOF")
        self.assertEqual(cm.exception.code, None)

    def test_do_help(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.assertTrue(mock_stdout.getvalue().strip() != "")

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel")
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    def test_do_destroy(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    def test_do_all(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all")
            self.assertIn(str([]), mock_stdout.getvalue())

    def test_do_update(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel")
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    def test_custom_prompt(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.prompt = "(custom_prompt) "
            self.console.onecmd("prompt")
            self.assertEqual(mock_stdout.getvalue().strip(), "(custom_prompt)")

if __name__ == '__main__':
    unittest.main()