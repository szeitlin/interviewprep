"""You are in charge of the cake for your niece's birthday 
and have decided the cake will have one candle for each year 
of her total age. When she blows out the candles, she’ll 
only be able to blow out the tallest ones. Your task is to 
find out how many candles she can successfully blow out."""

import os

def birthdayCakeCandles(ar):
    """
    Find the max, then count how many are the max. 
    Print that out
    :param ar: list
    :return: integer
    """
    tallest = max(ar)
    count = 0
    for candle in ar:
        if candle==tallest:
            count+=1
    print(count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()