"""John works at a clothing store. 
He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.
For example, there are  socks with colors . 
There is one pair of color  and one of color . 
There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. 
It must return an integer representing the number of matching pairs of socks 
that are available.

sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock
Input Format
The first line contains an integer , the number of socks represented in . 
The second line contains  space-separated integers describing the colors  of the socks in the pile.
Constraints

 where 
Output Format
Return the total number of matching pairs of socks that John can sell.
Sample Input
9
10 20 20 10 10 30 50 10 20
Sample Output
3
"""

def parse_outside_input(self):
    '''
    Read input
    :return: n, ar
    '''
    n = int(input())
    ar = map(int, input().rstrip().split())

class SockMatcher:

    def __init__(self, n, ar):
        '''
        
        :param n: (int) number of socks in the pile
        :param ar: (list) array of colors of the socks
        '''
        self.n =n
        self.ar = ar

    def iterative_counting(self):
        '''
        count and group
        :return: 
        '''
        socks = dict()

        for color in self.ar:
            if color in socks:
                socks[color] += 1
            else:
                socks.update({color:1})
        print(socks)
        return socks

    def calculate_pairs(self, socks):
        '''
        Ignore spare socks
        :return: (int) number of pairs
        '''
        pair_count = 0
        for color in socks:
            pair_count += socks[color] // 2

        print(pair_count)
        return pair_count
