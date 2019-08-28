#!/bin/python3

import os


# Complete the makeAnagram function below.
def make_anagram(a:str, b:str) -> int:
    """
    Count number of characters to delete to make the strings anagrams
    :param a: a string
    :param b: another string
    :return: integer number of characters to delete
    """
    b_list = [y for y in b]
    overlap, extra = [], []

    for i,char in enumerate(a):
        if char in b_list:
            overlap.append(char)
            b_list.remove(char)
        else:
            extra.append(char)

    print("overlap:{}".format(overlap))
    print("extra:{}".format(extra))
    return len(extra + b_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = make_anagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()