import unittest2
from counting_valleys import ValleyCounter

class TestBaseCases(unittest2.TestCase):

    def test_no_valleys(self):
        n = 2
        s = 'UD'
        vc = ValleyCounter(n, s)
        hike = vc.convert_path()
        assert hike == 0

    def test_one_valley(self):
        n = 2
        s = 'DU'
        vc = ValleyCounter(n, s)
        hike = vc.convert_path()
        assert hike == 1

    def test_example(self):
        n = 8
        s = 'UDDDUDUU'
        vc = ValleyCounter(n, s)
        hike = vc.convert_path()
        assert hike == 1

    def test_end_down(self):
        n = 3
        s = 'UDU'
        vc = ValleyCounter(n, s)
        hike = vc.convert_path()
        assert hike == 0

    def test_end_up(self):
        n = 3
        s = 'DUD'
        vc = ValleyCounter(n, s)
        hike = vc.convert_path()
        assert hike == 1

if __name__ == '__main__':
    unittest2.main()
