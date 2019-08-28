import os

def maximumToys(prices:list, k:int) -> int:
    """
    Want the max number of toys Mark can buy within his budget
    :param prices: list of int
    :param k: budget (int)
    :return: length of the list corresponding to the toys Mark can buy (int)
    """
    chosen = []
    for item in sorted(prices):
        if (total + item) <= k:
            total += item
            chosen.append(item)
        else:
            continue

    maxtoys = len(chosen)

    return maxtoys



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
