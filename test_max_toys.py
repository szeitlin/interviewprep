import unittest2

class TestMaxToys(unittest2.TestCase):

    def test_example(self):
        """this is the slow way"""
        k = 50
        prices = [1,12,5,111,200,1000,10]
        total = 0
        chosen = []
        for item in sorted(prices):
            if (total + item) <= k:
                total += item
                chosen.append(item)
            else:
                continue

        maxtoys = len(chosen)
        assert maxtoys == 4

if __name__ == '__main__':
    unittest2.main()