from unittest import TestCase
from LongestWordFinder import LongestWordFinder
__author__ = 'Akshay'


class TestLongestWordFinder(TestCase):

    def setUp(self):
        self.finder = LongestWordFinder('words.txt')

    def test_load_file_information(self):
        self.finder.load_file_information()
        print self.finder.lengthWordsMap
        self.assertIsNotNone(self.finder.lengthWordsMap)

    def test_generate_substrings_of_word(self):
        subStrings = self.finder.generate_substrings_of_word('ratcatdogcat')
        for subSting in subStrings:
            print subSting
            self.assertIsNotNone(subSting)

    def test_determine_longest_word(self):
        longestWordList = self.finder.determine_longest_word()
        print longestWordList
        self.assertEqual(longestWordList[0],'ratcatdogcat')