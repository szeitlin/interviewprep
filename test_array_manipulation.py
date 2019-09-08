import unittest2
from arrayManipulation import arrayManipulation

class TestExample(unittest2.TestCase):

    def test_one_example(self):
        """doing it this way works, but it's too slow"""
        n = 5
        queries = [[1,2,100],
                   [2,5,100],
                   [3,4,100]]
        #make a list of zeros
        arr = [0]*n
        #convert the indices and use those to add k
        for q in queries:
            a = q[0] - 1
            b = q[1] - 1
            k = q[2]

            for i in range(a,b+1):
                arr[i] += k
        print(arr)
        assert max(arr) == 200

    def test_method(self):
        n = 10
        queries = [[1,5,3],
                    [4,8,7],
                    [6,9,1]]
        result = arrayManipulation(n, queries)
        assert result == 10

if __name__ == '__main__':
    unittest2.main()
