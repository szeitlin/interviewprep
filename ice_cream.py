"""
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, 
they pool their money to buy ice cream. 
On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of money and the cost of each flavor for t trips to the Ice Cream Parlor, 
help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money 
during each visit. 

ID numbers are the 1- based index number associated with a cost. 

For each trip to the parlor, print the ID numbers for the two types of ice cream 
that Sunny and Johnny purchase as two space-separated integers on a new line. 
You must print the smaller ID first and the larger ID second.

For example, there are n=5 flavors having cost = [2,1,3,5,6]. 
Together they have money=5 to spend. 
They would purchase flavor ID's 1 and 3 for a cost of 2 + 3 = 5. 
Use 1-based indexing for your response.

Note:
Two ice creams having unique IDs  and  may have the same cost. 
There will always be a unique solution.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    """
    Find the two unique items in cost array that sum to exactly money amount
    Return the IDs (1-indexed position in cost array) as a string
    
    :param cost: array of int
    :param money: int
    :return: string with space-separated integer IDs 
    """
    #need to get combinations and subtract from the total
    #have to do it by index

    id_list = []

    # want to loop through and restart if first item needs to be excluded
    #import ipdb; ipdb.set_trace()

    for i in range(len(cost)):
        if len(id_list)==2:
            if sum([cost[id_list[0]],cost[id_list[1]]]) == money:
                break
        else:
            cost = cost[i:]
            wallet = money
            id_list = []
            for i, amount in enumerate(cost):
                print("amount is {}".format(amount))
                if (wallet - amount) >= 0:
                    id_list.append(i)
                    if (wallet - amount) == 0:
                        break
                    else:
                        wallet -= amount
                        print("remaining money is {}".format(wallet))
                else:
                    if len(id_list)==2:
                        break

    result = " ".join([str((x+1)) for x in id_list]) #convert to 1-indexed at the end
    print(result)
    return result




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)