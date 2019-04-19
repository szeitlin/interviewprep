"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
Given an integer, n, find and print the number of letter a's in the first n letters 
of Lilah's infinite string.
For example, if the string s='abcac' and n=10, the substring we consider is 'abcacabcac', 
the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

Function Description
Complete the repeatedString function in the editor below. 
It should return an integer representing the number of occurrences of a 
in the prefix of length n in the infinitely repeating string.

repeatedString has the following parameter(s):
s: a string to repeat
n: the number of characters to consider
Input Format
The first line contains a single string, s. 
The second line contains an integer, n.

Constraints
1<= s <= 100
1 <=n <= 10^12
for 25% of the test cases, n < 1M

Output Format
Print a single integer denoting the number of letter a's in the first n letters 
of the infinite string created by repeating s infinitely many times.

Sample Input 0
aba
10
Sample Output s
7

Sample Input 1
a
1000000000000

Sample Output 1
1000000000000

Explanation 1 
Because all of the first 1000000000000 letters of the infinite string are a, 
we print 1000000000000 on a new line.
"""
def parse_outside_input():
    """
    :return: s (str) and n (int)
    """
    s = input()

    n = int(input())
    return s, n

class RepeatCounter:

    def __init__(self, s, n):
        """
        :param s: (str) substring that repeats n times
        :param n: (int) number of letters of the infinite string to count a's in 
        """
        self.s = s
        self.n = n

    def a_counter(self):
        """
        Count the number of a's in the string that is n letters long. 
        :return: (int)
        """

        if 'a' not in self.s:
            return 0
        elif self.s == 'a':
            return self.n
        else:
            #smarter way where you just calculate it instead of materializing the str
            a_per_substr = sum([1 for x in self.s if x =='a'])
            complete_repeats = self.n//len(self.s)
            complete_repeat_counts = complete_repeats * a_per_substr

            remaining_letters = self.n - (len(self.s) * complete_repeats)
            substr = self.s[0:remaining_letters]
            additional = sum([1 for x in substr if x =='a'])

            total = complete_repeat_counts + additional

        return total
