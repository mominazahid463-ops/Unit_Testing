import unittest
from string_utils import format_slug, reverse_and_clean, get_initials

class TestStringUtils(unittest.TestCase):

    # No specific class instantiation needed for static string functions,
    # but we can use setUp for data consistency if needed.
    def setUp(self):
        self.sample_name = "John Quincy Doe"
        self.sample_text = "Hello World 123!"

    def tearDown(self):
        pass

    # Tests for format_slug
    def test_format_slug_normal(self):
        self.assertEqual(format_slug("Hello World"), "hello-world")

    def test_format_slug_edge_case(self):
        # Testing multiple spaces and special characters
        self.assertEqual(format_slug("  Python   @#$   Rules  "), "python-rules")

    def test_format_slug_error(self):
        with self.assertRaises(ValueError):
            format_slug("   ")
        with self.assertRaises(TypeError):
            format_slug(101)

    # Tests for reverse_and_clean
    def test_reverse_and_clean_normal(self):
        self.assertEqual(reverse_and_clean("abc"), "cba")

    def test_reverse_and_clean_removes_digits(self):
        # Testing removal of numbers during reversal
        self.assertEqual(reverse_and_clean("Python3"), "nohtyP")

    def test_reverse_and_clean_error(self):
        with self.assertRaises(TypeError):
            reverse_and_clean(None)

    # Tests for get_initials
    def test_get_initials_normal(self):
        self.assertEqual(get_initials(self.sample_name), "JQD")

    def test_get_initials_lowercase_input(self):
        # Testing if it handles lowercase and converts to uppercase initials
        self.assertEqual(get_initials("alan turing"), "AT")

    def test_get_initials_error(self):
        with self.assertRaises(ValueError):
            get_initials("")

if __name__ == '__main__':
    unittest.main()