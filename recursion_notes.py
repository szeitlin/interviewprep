
def recurse(cloudlist, jumps):
    print(f'cloudlist is {cloudlist} and jumps is {jumps}')

    if len(cloudlist) > 1:
        jumps += 1
        return recurse(cloudlist[1:], jumps) #have to explicitly say return when calling recurse

    return jumps

jumps = recurse(cloudlist, jumps)
cloudlist is [1, 2, 3] and jumps is 0
cloudlist is [2, 3] and jumps is 1
cloudlist is [3] and jumps is 2

In [20]: jumps
Out[20]: 1

#why is the return value different from the printed output? (and how is it lower?)