import unittest2
from ice_cream import whatFlavors

#first line is money
#second line is n, the size of the cost array
#third line contains the cost array

class TestInput(unittest2.TestCase):

    def test_example_input_hardcoded(self):
        """Correct answer skips two and are sequential"""
        money = 4
        cost = [1,4,5,3,2]
        result = whatFlavors(cost, money)
        assert result == "1 4"
        money2 = 4
        cost2 = [2,2,4,3]
        result2 = whatFlavors(cost2, money2)
        assert result2 == "1 2"

    def test_harder_example(self):
        """
        this one requires a restart to exclude the first
        """
        money = 4
        cost = [1,2,2]
        result = whatFlavors(cost, money)
        assert result == "2 3"

    def test_sample_test2a(self):
        """
        Both skipping initial and intermediate
        """
        money = 8
        cost = [4, 3, 2, 5, 7]
        result = whatFlavors(cost, money)
        assert result == "2 4"

    def test_sample_test2b(self):
        money = 12
        cost = [7, 2, 5, 4, 11]
        result = whatFlavors(cost, money)
        assert result == "1 3"

class TestBigFile(unittest2.TestCase):

    def test_big_example1(self):
        with open('ice_cream_testcase.txt', 'r') as f:
            num_trips = int(f.readline())
            assert num_trips == 34
            money = int(f.readline())
            assert money == 585167982
            cost_len = int(f.readline())
            assert cost_len == 21617
            for i in range(1):                 #(num_trips):
                trip = list(map(int, f.readline().rstrip().split()))
                assert len(trip) == cost_len
                result = whatFlavors(trip, money)
                print(result)

if __name__ == '__main__':
    unittest2.main()