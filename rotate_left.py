"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
For example, if 2 left rotations are performed on array [1,2,3,4,5], 
then the array would become [3,4,5,1,2].
Given an array a of n integers and a number, d, 
perform  left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers.

Function Description
Complete the function rotLeft in the editor below. 
It should return the resulting array of integers.

rotLeft has the following parameter(s):
An array of integers a.
An integer d, the number of rotations.

Input Format
The first line contains two space-separated integers n and d, 
the size of a and the number of left rotations you must perform. 
The second line contains n space-separated integers a[i].

Constraints
1 <= n <= 10^5
1 <= d <= n
1 <= a[i] <= 1M


Output Format
Print a single line of n space-separated integers 
denoting the final state of the array after performing  left rotations.

Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4

Explanation
When we perform 4 left rotations, the array undergoes the following sequence of changes:
[1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2] -> [4,5,1,2,3] -> [5,1,2,3,4] 
"""
def parse_outside_input():
    """
    nd is the first row, where
    n is the the size of a
    d is the number of left rotations to perform
    a is the array itself, as a space-delimited string
    :return: only need d and a for the actually method
    """

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, input().rstrip().split())

    return d, a

class LeftRotator:

    def __init__(self, d, a):
        """
        :param d: number of rotations to perform (int)
        :param a: list of integers
        """
        self.d = d
        self.a = a

    def rotLeft(self):
        """
        :returns: the rotated list (as a space-delimited string, apparently)
        """
        #don't want to actually materialize all the intermediate steps
        if len(self.a) == 1:
            return str(self.a[0])

        else:
            if self.d < len(self.a):
                rotated = self.a[self.d:] + self.a[0:self.d]
            if self.d > len(self.a):
                actual = self.d%len(self.a) #use the remainder
                rotated = self.a[actual:] + self.a[0:actual]

            return ' '.join([str(x) for x in rotated])
