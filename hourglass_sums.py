"""
Given a 6x6 2D array arr, there are 16 hourglasses; 
sum each of them and print the biggest sum

example:
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

we calculate: 
-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18

max sum is 28

"""
#!/bin/python3

import os

# Complete the hourglassSum function below.
def hourglassSum(arr):
    """
    Each of the 6 lines of inputs contains 6 space-separated integers 
    :param arr: str
    :return: int (the maximum hourglass sum)
    """
    sums = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            one =  arr[i][j] +  arr[i][j + 1] +  arr[i][j + 2]
            two =  arr[i + 1][j + 1]
            three =  arr[i + 2][j] +  arr[i + 2][j + 1] +  arr[i + 2][j + 2]
            total = one + two + three
            sums.append(total)
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()