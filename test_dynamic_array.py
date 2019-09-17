import unittest2
from dynamic_array import dynamicArray

class TestExample(unittest2.TestCase):

    def test_example1(self):
        input = """ 2 5
                    1 0 5
                    1 1 7
                    1 0 3
                    2 1 0
                    2 1 1
                """
        #parse input into n, queries
        split_input = [int(x) for x in input.split()]

        #first line is N number of lists to put in seqList
        #followed by Q, the number of queries
        n = split_input[0]
        assert n == 2
        querycount = split_input[1]
        assert querycount == 5

        queries = [split_input[2:][x:x+3] for x in range(0,querycount)]

        seqList = [[] for i in range(n)]
        lastAnswer = 0
        results = []

        for sublist in queries:
            querytype = sublist[0]
            x = sublist[1]
            y = sublist[2]
            if querytype == 1:
                listindex = (x^lastAnswer)%n
                seqList[listindex].append(y)
                print(seqList)
            elif querytype == 2:
                listindex = (x^lastAnswer)%n
                lastAnswer = seqList[listindex][y % (len(seqList))]
                print(lastAnswer)
                results.append(lastAnswer)
        print(results)
        assert results == [7,3]

if __name__ == '__main__':
    unittest2.main()