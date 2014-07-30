import re
import os
import logging
from collections import defaultdict

__author__ = 'Akshay'

DEFAULT_MAX = 0
DEFAULT_MIN = 0
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FILE_LOCATION = 'LongestWordFinder.log'
DEFAULT_FILE_LOCATION = "wordsforproblem.txt"


class LongestWordFinder(object):

    def __init__(self, location=DEFAULT_FILE_LOCATION):
        """Default Constructor"""
        self.log = logging.getLogger('LongestWordFinder')
        self.fileLocation = location
        self.lengthWordsMap = defaultdict(list)
        self.load_file_information()
        self.maxWordLength = max(self.lengthWordsMap.iterkeys())
        self.minStringLength = min(self.lengthWordsMap.iterkeys())
        self.longestWords = []

    def load_file_information(self):
        """
        Read the file containing sorted list of words. Create a map, length
        of an word as key and append the word as value.
        """
        if os.path.isfile(self.fileLocation):
            with open(self.fileLocation, 'r') as fileDescriptor:
                self.log.info("Opened file at location: %s"%self.fileLocation )
                for line_no, line in enumerate(fileDescriptor):
                    word = line.strip()
                    self.lengthWordsMap[len(word)].append(word)
            fileDescriptor.close()

        self.log.debug(self.lengthWordsMap)
        return self.lengthWordsMap

    def generate_substrings_of_word(self,word):
        """
        Generate all substring of a given word.
        """
        wordCharArray = tuple(word)
        comboFound = set()
        for size in range(self.minStringLength, len(wordCharArray)+1-self.minStringLength):
            for index in range(len(wordCharArray)+1-size):
                subArray = word[index:index+size]
                if subArray not in comboFound:
                    comboFound.add(set)
                    yield subArray

    def determine_longest_word(self):
        """
        Generate all substring of a given word.
        """

        sortedLengthWordsMap = sorted(self.lengthWordsMap.iteritems(),key=lambda (k,v):k, reverse=True)
        self.log.debug(sortedLengthWordsMap)

        for length, words in sortedLengthWordsMap:
            self.log.debug("Started the check for longest word for length: %d"%length)
            for word in words:
                temp = word
                wrdLength = len(word)
                subStrings = self.generate_substrings_of_word(temp)

                for subStr in subStrings:
                    self.log.debug("SubStrings: %s"%subStr)
                    subWordLength = len(subStr)
                    if (self.lengthWordsMap.has_key(subWordLength)) and not (subWordLength == wrdLength):
                        self.log.debug(word)
                        if (subStr in self.lengthWordsMap[subWordLength]):
                            word = re.sub(subStr, '', word)
                            if word == '':
                                self.log.info("Found word: %s"%temp)
                                self.longestWords.append(temp)
                                break

        return self.longestWords


if __name__ == "__main__":
    logging.basicConfig(filename=DEFAULT_LOG_FILE_LOCATION, level=DEFAULT_LOG_LEVEL)
    logging.StreamHandler()
    obj=LongestWordFinder()
    longestWordList = obj.determine_longest_word()
    print ("1st Longest word: %s" %longestWordList[0])
    print ("2nd Longest word: %s" %longestWordList[1])
    print ("Total Longest word: %d" %len(longestWordList))




