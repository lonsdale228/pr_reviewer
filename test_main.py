import unittest
from unittest.mock import patch
import io

from main import print_hi


class TestPrintHi(unittest.TestCase):
    """Tests for the print_hi function as changed in this PR.

    The PR changed print_hi to include `assert tet` before the print
    statement. Since 'tet' is not defined anywhere in the module, any
    call to print_hi raises a NameError before reaching the print.
    """

    def test_raises_name_error(self):
        """print_hi raises NameError because 'tet' is not defined."""
        with self.assertRaises(NameError):
            print_hi("Alice")

    def test_name_error_references_tet(self):
        """The NameError message references the undefined name 'tet'."""
        with self.assertRaises(NameError) as ctx:
            print_hi("Alice")
        self.assertIn("tet", str(ctx.exception))

    def test_raises_name_error_with_empty_string(self):
        """NameError is raised regardless of the name argument (empty string)."""
        with self.assertRaises(NameError):
            print_hi("")

    def test_raises_name_error_with_none(self):
        """NameError is raised regardless of the name argument (None)."""
        with self.assertRaises(NameError):
            print_hi(None)

    def test_raises_name_error_with_numeric_name(self):
        """NameError is raised regardless of the name argument (integer)."""
        with self.assertRaises(NameError):
            print_hi(42)

    def test_print_is_never_called(self):
        """print is never invoked because NameError occurs before the print statement."""
        with patch("builtins.print") as mock_print:
            with self.assertRaises(NameError):
                print_hi("Bob")
            mock_print.assert_not_called()

    def test_raises_name_error_not_assertion_error(self):
        """The exception is a NameError, not an AssertionError, because 'tet' is undefined."""
        with self.assertRaises(NameError):
            print_hi("test")
        # Confirm AssertionError is not raised instead
        try:
            print_hi("test")
        except NameError:
            pass
        except AssertionError:
            self.fail("print_hi raised AssertionError instead of NameError")

    def test_no_output_produced(self):
        """No text is written to stdout when print_hi is called."""
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            with self.assertRaises(NameError):
                print_hi("Charlie")
            self.assertEqual(mock_stdout.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
