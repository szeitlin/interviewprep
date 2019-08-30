#!/bin/python3

import os

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    """
    find and print the minimum absolute difference between any two elements in the array
    :param arr: list of integers
    :return: int
    """
    ordered = sorted(arr)
    minDiff = ordered[-1] - ordered[0] #initialize with max amount

    for i in range(len(arr) - 1):
        diff = abs(ordered[i+1] - ordered[i])
        print(diff)
        if diff < minDiff:
            minDiff = diff
        else:
            continue
    return minDiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()