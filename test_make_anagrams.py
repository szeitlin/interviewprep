import unittest2
from make_anagrams import make_anagram

class TestShortExamples(unittest2.TestCase):

    def test_single_mismatch(self):
        a = 'ab'
        b = 'bc'
        #look for overlap
        a_set = set([x for x in a])
        b_set = set(y for y in b)
        overlap = len(a_set & b_set)
        deletions = len(a) + len(b) - (2*overlap)
        assert deletions == 2

    def test_multiple_mismatch(self):
        a = 'cde'
        b = 'abc'
        deletions = make_anagram(a,b)
        assert deletions == 4

    def test_different_lengths_and_repeated_chars(self):
        a = 'bba'
        b = 'ac'
        deletions = make_anagram(a,b)
        assert deletions == 3

class TestLongerExamples(unittest2.TestCase):

    def test_repeated_chars(self):
        a = 'jjilmmm'
        b = 'liyyymm'
        deletions = make_anagram(a,b)
        assert deletions == 6

    def test_different_lengths_and_repeated_chars(self):
        a = 'fcrxzwscanmligyxyvym'
        b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
        deletions = make_anagram(a,b)
        assert deletions == 30

if __name__ == '__main__':
    unittest2.main()
