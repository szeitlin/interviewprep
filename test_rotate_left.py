import unittest2
from rotate_left import LeftRotator

class TestExamples(unittest2.TestCase):

    def test_given_five_four(self):
        d = 4
        a = [1,2,3,4,5]
        lr = LeftRotator(d,a)
        result = lr.rotLeft()
        assert result == "5 1 2 3 4"

    def test_given_one(self):
        d = 2
        a = [0]
        lr = LeftRotator(d,a)
        result = lr.rotLeft()
        assert result == "0"

    def test_given_five_one(self):
        d = 1
        a = [1,2,3,4,5]
        lr = LeftRotator(d,a)
        result = lr.rotLeft()
        assert result == "2 3 4 5 1"

    def test_rotate_one(self):
        d = 1
        a = [3,2,4]
        lr = LeftRotator(d,a)
        result = lr.rotLeft()
        assert result == "2 4 3"

    def test_rotate_many(self):
        d = 10
        a = [1,2,3]
        lr = LeftRotator(d,a)
        result = lr.rotLeft()
        print(result)
        assert result == "2 3 1"

if __name__ == '__main__':
    unittest2.main()