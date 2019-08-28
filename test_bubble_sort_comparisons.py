import unittest2
from bubble_sort_comparisons import count_swaps

class TestCountSwaps(unittest2.TestCase):

    def test_no_sort(self):
        n = 3
        a = [1,2,3]
        result = count_swaps(n, a)
        assert result == (0,1,3)

    def test_backwards(self):
        n = 3
        a = [3,2,1]
        result = count_swaps(n, a)
        assert result == (3,1,3)

    def test_scrambled(self):
        n = 4
        a = [4,2,3,1]
        result = count_swaps(n, a)
        assert result == (5,1,4)
        
if __name__ == '__main__':
    unittest2.main()