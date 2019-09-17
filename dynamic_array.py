"""
create a list, seqList, of N empty lists 
from 0 - N-1
create an integer lastAnswer and initialize it to 0
there are 2 types of queries to be performed on the list of lists
1) find the list at index ((x ^ lastAnswer) % N
    append integer y to that list
2) find the list at index ((x ^ lastAnswer) % N
    find the value of the element in the list) at y % size (where size is len(list) and assign it to lastAnswer
    print the new value of lastAnswer on a new line
"""

#!/bin/python3

import os


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n:int, queries:list):
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    results = []
    for sublist in queries:
        querytype = sublist[0]
        x = sublist[1]
        y = sublist[2]
        if querytype == 1:
            listindex = x^lastAnswer % n
            seqList[listindex].append(y)
        elif querytype == 2:
            listindex = x ^ lastAnswer % n
            lastAnswer = y % (len(seqList[listindex]))
            results.append(lastAnswer)
    print(results)
    return results

