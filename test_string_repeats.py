import unittest2
from string_repeats import RepeatCounter

class TestACounter(unittest2.TestCase):

    def test_smart_way_short(self):
        s = 'aba'
        n = 10
        rc = RepeatCounter(s, n)
        counts = rc.a_counter()
        assert counts == 7

    def test_smart_way_longer(self):
        s = 'a'
        n = 1000000000000
        rc = RepeatCounter(s, n)
        counts = rc.a_counter()
        assert counts == n

    def test_smart_way_longer_str(self):
        s = 'abcac'
        n = 300000000
        rc = RepeatCounter(s, n)
        counts = rc.a_counter()
        assert counts == 120000000

    def test_smart_way_even_number(self):
        s = 'abcc'
        n = 35
        rc = RepeatCounter(s, n)
        counts = rc.a_counter()
        assert counts == 9

    def test_no_a(self):
        s = 'x'
        n = 22
        rc = RepeatCounter(s, n)
        counts = rc.a_counter()
        assert counts == 0

if __name__ == '__main__':
    unittest2.main()