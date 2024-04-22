#!/usr/bin/python3
"""Test module for HBNBCommand class"""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
sys.path.append("..")
import models
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()
        self.storage_patcher = patch('models.storage')
        self.storage_mock = self.storage_patcher.start()

    def tearDown(self):
        """Tear down test environment"""
        self.storage_patcher.stop()

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            expected_output = (
                "Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help"
                "  quit  show  update"
            )
            HBNBCommand().onecmd("help")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        """Test show command"""
        with patch('builtins.input', side_effect=['show BaseModel', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** instance id missing **",
                          mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        """Test destroy command"""
        with patch('builtins.input', side_effect=['destroy BaseModel', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** instance id missing **",
                          mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("quit")
            self.assertEqual(mock_stdout.getvalue().strip(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_base_model_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_city_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show City")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_amenity_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Amenity")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_place_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Place")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_review_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Review")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_state_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show State")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_user_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show User")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("update")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("destroy")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_base_model_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(
                output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_user_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create User")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(
                output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_place_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Place")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(
                output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_city_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create City")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(
                output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_state_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create State")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(
                output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_review_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Review")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(
                output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_amenity_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Amenity")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(
                output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        """Test module for HBNBCommand class"""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(
                output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        """Test update command"""
        with patch('builtins.input', side_effect=['update BaseModel', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        """Test create command with invalid class"""
        with patch('builtins.input',
                   side_effect=['create InvalidClass', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        """Test show command with invalid class"""
        with patch('builtins.input', side_effect=['show InvalidClass', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        """Test destroy command with invalid class"""
        with patch('builtins.input',
                   side_effect=['destroy InvalidClass', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        """Test update command with invalid class"""
        with patch('builtins.input',
                   side_effect=['update InvalidClass', 'EOF']):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    def test_create_missing_class(self):
        """Test module for HBNBCommand class"""
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        """Test module for HBNBCommand class"""
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_do_create(self):
        """Test for do_create method."""
        # Test class name missing
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(HBNBCommand().onecmd('create'))
            self.assertEqual(fake_out.getvalue().strip(), "** class name missing **")

        # Test class doesn't exist
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(HBNBCommand().onecmd('create UnknownClass'))
            self.assertEqual(fake_out.getvalue().strip(), "** class doesn't exist **")

        # Test creating State instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(HBNBCommand().onecmd('create State name="California"'))
            self.assertIsNotNone(models.storage.all()['State.California'])

        # Test creating Place instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(HBNBCommand().onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297'))
            self.assertIsNotNone(models.storage.all()['Place.My_little_house'])
if __name__ == '__main__':
    unittest.main()
