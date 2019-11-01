"""Given five positive integers, 
find the minimum and maximum values that can be calculated 
by summing exactly four of the five integers. 
Then print the respective minimum and maximum values 
as a single line of two space-separated long integers."""

def miniMaxSum(arr):
    """
    
    :param arr: list
    :return: print two space-separated integers
    """
    ordered = sorted(arr)
    mini = sum(ordered[0:4])
    maxi = sum(ordered[1:])
    print("{} {}".format(mini,maxi))
    return [mini,maxi]


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)