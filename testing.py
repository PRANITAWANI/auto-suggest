import unittest

from auto_suggest import auto_suggest # type: ignore


class Testauto_suggest(unittest.TestCase):
    def test_exact_substring_match(self):
        words = ['take', 'make', 'check', 'ack', 'rake']
        subtext = 'ke'
        expected_result = ['take', 'make', 'rake']
        self.assertEqual(auto_suggest(words, subtext), expected_result)

    def test_wildcard_match(self):
        words = ['take', 'make', 'check', 'ack', 'rake']
        subtext = '*k'
        expected_result = ['check', 'ack']
        self.assertEqual(auto_suggest(words, subtext), expected_result)

    def test_no_match(self):
        words = ['take', 'make', 'check', 'ack', 'rake']
        subtext = 'xyz'
        expected_result = []
        self.assertEqual(auto_suggest(words, subtext), expected_result)

    def test_case_insensitive_match(self):
        words = ['Take', 'Make', 'check', 'aCk', 'RaKe']
        subtext = 'tA'
        expected_result = ['Take']
        self.assertEqual(auto_suggest(words, subtext), expected_result)

    def test_empty_input(self):
        words = []
        subtext = '*k'
        expected_result = []
        self.assertEqual(auto_suggest(words, subtext), expected_result)

if __name__ == '__main__':
    unittest.main()
