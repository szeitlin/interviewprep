#!/bin/python3

import os


def arrayManipulation(n, queries):
    """
    Starting with a 1-indexed array of zeros and a list of operations, 
    for each operation add a value to each of the array element between 
    two given indices, inclusive. Once all operations have been performed, 
    return the maximum value in your array.
    :param n: length of the array
    :param queries: a 2d array of queries, 
    where each queries[i] contains three integers, a, b, and k.
    Add the values of k between the indices a and b inclusive (inclusive on both ends)
    :return: the max value of the array
    """
    arr = [0] * n
    for q in queries:
        a = q[0] - 1
        b = q[1] - 1
        k = q[2]
        for i in range(a, b + 1):
            arr[i] += k
    return max(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()