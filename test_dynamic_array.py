import unittest2
from dynamic_array import dynamicArray

class TestSample(unittest2.TestCase):

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
        querycount = split_input[1] #don't actually need this
        assert querycount == 5

        querylist = split_input[2:]
        print("querylist {}".format(querylist))
        queries = [querylist[x:x+3] for x in range(0,len(querylist),3)]
        print("queries {}".format(queries))

        seqList = [[] for i in range(n)]
        lastAnswer = 0
        results = []

        for sublist in queries:
            querytype = sublist[0]
            x = sublist[1]
            y = sublist[2]
            if querytype == 1:
                listindex = (x^lastAnswer)%n
                print("listindex {}".format(listindex))
                seqList[listindex].append(y)
                print(seqList)
            elif querytype == 2:
                listindex = (x^lastAnswer)%n
                print("listindex {}".format(listindex))
                listsize = len(seqList[listindex])
                print("listsize {}".format(listsize))
                lastAnswer = seqList[listindex][y % listsize]
                print(lastAnswer)
                results.append(lastAnswer)
        print(results)
        assert results == [7,3]

class TestTestCases(unittest2.TestCase):

    def test_testcase(self):
        with open('dynamic_array_test_cases.txt', 'r') as f:
            raw = f.readlines()

        firstline = [int(x) for x in raw[0].split()]
        n = firstline[0]
        querycount = firstline[1] #not using this
        queries = []

        for line in raw[1:]:
            queries.append([int(x) for x in line.split()])

        print(queries[0:10])
        result = dynamicArray(n, queries)
        print("result\n")
        print(result)
        #todo: have to flatten this
        #flat_result = [j for i in result for j in i]

        with open('dynamic_array_expected_output.txt', 'r') as output:
            raw_output = output.readlines()

        formatted = [int(x.rstrip()) for x in raw_output]
        print("formatted\n")
        print(formatted)
        assert result == formatted


if __name__ == '__main__':
    unittest2.main()