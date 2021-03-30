import unittest

from full_name_parser import FullNameParser


class TestFullNameParser(unittest.TestCase):
    def test_html_without_correct_class(self):
        parser = FullNameParser('test_html/unvalid_data_1.html')
        self.assertEqual(parser.parse_html_to_get_required_tag(), [])

    def test_html_without_correct_tag(self):
        parser = FullNameParser('test_html/unvalid_data_2.html')
        self.assertEqual(parser.parse_html_to_get_required_tag(), [])

    def test_html_without_correct_class_name(self):
        parser = FullNameParser('test_html/unvalid_data_3.html')
        self.assertEqual(parser.parse_html_to_get_required_tag(), [])


if __name__ == '__main__':
    unittest.main()
