import unittest2
from candles import birthdayCakeCandles

class TestExample(unittest2.TestCase):

    def test_short(self):
        ar = [3,2,1,3]
        result = birthdayCakeCandles(ar)
        assert result == 2