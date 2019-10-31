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
from itertools import combinations

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    """
    Find the two unique items in cost array that sum to exactly money amount
    Return the IDs (1-indexed position in cost array) as a string
    
    Want to avoid having to check n! numbers of combinations
    
    :param cost: array of int
    :param money: int
    :return: string with space-separated integer IDs 
    """
    #indices = range(len(cost))
    #print("indices is {}".format(indices))

    #indexed_amounts = zip(indices, cost)
    #print("indexed_amounts is {}".format(indexed_amounts))
    # pairs = combinations(indexed_amounts, 2) #this is expensive on a long list
    # print(list(pairs))
    wallet = money
    print("wallet is {}".format(wallet))

   #4th version, here's how to get the pairs of indices, and short-circuit
   #the loop step if you don't need to check the whole thing:
    import ipdb; ipdb.set_trace()
    for i in range(len(cost)):
        for j in (range(i + 1, len(cost))):
            pair = (i, j)
            print(cost[i], cost[j])
            if cost[i] > money:
                print("too much! {}".format(cost[i]))
                continue
            else:
                try:
                    if cost[i] + cost[j] == money:
                        result = " ".join([str((x + 1)) for x in pair])
                        print(result)
                        return result
                except IndexError as e:
                    print(e)
                    print(pair)

    #3rd version, try with just limiting it to two items and do combinations
    # while pairs:
    #     try:
    #         #import ipdb; ipdb.set_trace()
    #         first, second = next(pairs)
    #         if first[1] + second[1] == money:
    #             winner = (first[0], second[0])
    #             result = " ".join([str((x + 1)) for x in winner])
    #             print(result)
    #             return result
    #     except Exception:
    #         break


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)