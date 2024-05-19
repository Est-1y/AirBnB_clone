#!/usr/bin/python3

"""Unnitest"""

import sys
import unittest
from console import HBNBCommand
from unittest.mock import patch
from models.base_model import BaseModel
from io import StringIO
from models import storage


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        """ """
        self.console.preloop()
        self._reset_storage()

    def tearDown(self):
        """ """
        self.console.postloop()
        self._reset_storage()

    def _reset_storage(self):
        """Reset storage"""
        storage.all().clear()
        storage.save()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, command,mock_stdout):
        self.console.onecmd(command)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    def test_create_show_destroy_all_update_commands(self):
        # do_reate
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.assertTrue(f'BaseModel.{obj_id}' in storage.all())
            
        obj = storage.all()[f'BaseModel.{obj_id}']

        # do_Show
        expected_output = str(obj) + '\n'
        self.assert_stdout(expected_output, "show BaseModel {}".format(obj.id))

        # do_destroy
        self.assert_stdout("", "destroy BaseModel {}".format(obj.id))
        self.assertNotIn(obj, storage.all().values())

        # do_all
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        expected_output = "[{}, {}]\n".format(str(obj1), str(obj2))
        self.assert_stdout(expected_output, "all BaseModel")
       
        # do_update
        self.assert_stdout(
            "",
            'update BaseModel {} name "New Name"'.format(obj1.id)
        )
        updated_obj = storage.all()['BaseModel.' + obj1.id]
        self.assertEqual(updated_obj.name, "New Name")

    def test_invalid_commands(self):
        self._reset_storage()

        # Invalid_create -command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "create InvalidClass")

        # Invalid_show -command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "show InvalidClass")

        # Invalid_destroy -command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "destroy InvalidClass")

        # Invalid_all -command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "all InvalidClass")

        # Invalid_update command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "update InvalidClass")

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line_quit_commands(self, mock_stdout):

        # Empty_line
        expected_output = ""
        self.assert_stdout(expected_output, "")

        # Quit_command
        self.assertTrue(self.console.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_commands(self, mock_stdout):
        expected_output = "Quit command to exit the program"
        self.assert_stdout(expected_output, "help quit")


if __name__ == '__main__':
    unittest.main()
