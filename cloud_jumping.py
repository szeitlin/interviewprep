"""
Emma is playing a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 

She can jump on any cumulus cloud having a number that is equal to the number of 
the current cloud plus 1 or 2. 

She must avoid the thunderheads. 

Determine the minimum number of jumps it will take Emma to jump from her starting postion 
to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 
if they must be avoided. For example, c = [0,1,0,0,0,1,0] indexed 0 to 6. She should avoid 
clouds 1 and 5. 

She could follow the following two paths: 0->2->4->6 (3 jumps) or 0->2->3->4->6 (4 jumps)

Function Description
Complete the jumpingOnClouds function in the editor below. 
It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):
n: the total number of clouds (where 2 <= n <= 100)
c: an array of binary integers where you always start and end on a 0 (at least I think 
that's what they mean by c[0] = c[n-1] = 0)

sample input:
7
0 0 1 0 0 1 0

#looks like it's: 0->1->3->4->6

sample output:
4

sample input:
6
000010

#0->2->3->5

output:
3
"""
def parse_outside_input(self):
    '''
    Read input
    :return: n, c
    '''
    n = int(input())
    c = map(int, input().rstrip().split())

class CloudJumper:

    def __init__(self, n, c):
        '''
        
        :param n: the total number of clouds (where 2 <= n <= 100)
        :param c: an array of binary integers 
                  where you always start and end on a 0 (at least I think 
                  that's what they mean by c[0] = c[n-1] = 0)
        '''
        self.n = n
        self.c = c

    def jump_clouds(self):
        '''
        Can jump on 0 only, and can take only 1 or 2 steps at a time
        
        note: assume first cloud and last cloud are always 0 
        
        :return: (int) number of jumps
        '''
        jumps = 0

        def recurse(cloudlist, jumps):
            '''
            Recursively step through
            stop when on the last cloud
            :param cloudlist: remaining clouds
            :return: cloudlist, jumps (int)
            '''
            print(f'jumps is now: {jumps}')

            while len(cloudlist) >= 1:
                print(f'Cloudlist is now: {cloudlist}')
                if cloudlist == [0]:
                    break

                elif len(cloudlist) > 1 and (cloudlist[0] == 0) and (cloudlist[1] == 0):
                    jumps += 1
                    return recurse(cloudlist[2:], jumps)
                elif len(cloudlist) > 1 and (cloudlist[0] == 1):
                    jumps += 1
                    return recurse(cloudlist[1:], jumps)
                else:
                    return recurse(cloudlist[1:], jumps)

            return jumps

        jumps = recurse(self.c, jumps)
        return jumps

