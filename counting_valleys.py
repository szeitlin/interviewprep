"""
Gary is an avid hiker. 
He tracks his hikes meticulously, paying close attention to small details 
like topography. During his last hike he took exactly  steps. 
For every step he took, he noted if it was an uphill, or a downhill,  step. 
Gary's hikes start and end at sea level and each step up or down represents 
a  unit change in altitude. 

We define the following terms:
A mountain is a sequence of consecutive steps above sea level, 
starting with a step up from sea level and ending with a step down to sea level.

A valley is a sequence of consecutive steps below sea level, 
starting with a step down from sea level and ending with a step up to sea level.

Given Gary's sequence of up and down steps during his last hike, 
find and print the number of valleys he walked through.

For example, if Gary's path is s=[DDUUUUDD], 
he first enters a valley 2 units deep. 
Then he climbs out an up onto a mountain 2 units high. 
Finally, he returns to sea level and ends his hike.

Function Description
Complete the countingValleys function in the editor below. 
It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):
n: the number of steps Gary takes
s: a string describing his path

Input Format
The first line contains an integer , the number of steps in Gary's hike. 
The second line contains a single string of characters that describe his path.

Constraints
2 < 2 < 1M
steps are only U or D

Output Format
Print a single integer that denotes the number of valleys Gary walked through during his hike.
Sample Input
8
UDDDUDUU
Sample Output
1
Explanation
If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:
_/\      _
   \    /
    \/\/
He enters and leaves one valley.
"""
def parse_outside_input(self):
    '''
    Read input
    :return: n, ar
    '''
    n = int(input())
    s = input().split()
    return n, s

class ValleyCounter:

    def __init__(self, n, s):
        '''
        
        :param n: number of steps (int)
        :param s: the path (U up or D down) (str)
        '''
        self.n = n
        self.s = s

    def convert_path(self):
        '''
        Have to know what the previous step was at all times
        a valley is all consecutive steps below sea level
        let's also set sea level to 0, U to + and D to -
        '''
        level = 0
        convert = {'U':1, 'D':-1}
        translated = [convert.get(x) for x in self.s]
        print(translated)
        valley = False
        valley_count = 0

        for step in translated:
            level += step
            print(f'level is now: {level}')
            if level != 0:
                if (level < 0): #below sea level
                    valley = True
                elif (level > 0): #above sea level
                    valley = False
            else:
                if valley == True:
                    valley_count += 1
                else:
                    continue
        print(f'valley_count is now: {valley_count}')
        return valley_count
