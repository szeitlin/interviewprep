import unittest2
from sock_matches import SockMatcher

class TestSockMatcher(unittest2.TestCase):

    def test_sample1(self):
        n = 9
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        counter = SockMatcher(n, ar)
        socks = counter.iterative_counting()
        pair_count = counter.calculate_pairs(socks)
        assert pair_count == 3

    def test_iterative_counting(self):
        n = 9
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        counter = SockMatcher(n, ar)
        socks = counter.iterative_counting()
        assert socks == {10:4, 20:3, 30:1, 50:1}

    def test_empty(self):
        n = 0
        ar = []
        counter = SockMatcher(n, ar)
        socks = counter.iterative_counting()
        pair_count = counter.calculate_pairs(socks)
        assert pair_count == 0


if __name__ == '__main__':
    unittest2.main()

