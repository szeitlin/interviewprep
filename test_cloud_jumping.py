import unittest2
from cloud_jumping import CloudJumper

class TestExamples(unittest2.TestCase):

    def test_001(self):
        n = 4
        c = [0, 0, 1, 0]
        cj = CloudJumper(n, c)
        jumps = cj.jump_clouds()
        assert jumps == 2

    def test_010(self):
        n = 3
        c = [0, 1, 0]
        cj = CloudJumper(n, c)
        jumps = cj.jump_clouds()
        assert jumps == 1

    def test_7(self):
        n = 7
        c = [0, 0, 1, 0, 0, 1, 0]
        cj = CloudJumper(n, c)
        jumps = cj.jump_clouds()
        assert jumps == 4

    def test_6(self):
        n = 6
        c = [0, 0, 0, 0, 1, 0]
        cj = CloudJumper(n, c)
        jumps = cj.jump_clouds()
        assert jumps == 3

if __name__ == '__main__':
    unittest2.main()