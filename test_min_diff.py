import unittest2

from minDiff import minimumAbsoluteDifference

class TestMinDiff(unittest2.TestCase):

    def test_min_diff(self):
        test = [3, -7, 0]
        minDiff = minimumAbsoluteDifference(test)
        assert minDiff == 3

if __name__ == '__main__':
    unittest2.main()
