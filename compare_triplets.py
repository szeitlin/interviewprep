import itertools

def compareTriplets(a:list, b:list)-> list:
    """
    if a[i]>b[i], a gets 1 point
    converse is also true
    if a[i]==b[i], nothing happens

    a: list of 3 integers
    b: list of 3 integers
    returns: list of 2 integers
    """
    a_points, b_points = 0,0

    for a,b in itertools.zip_longest(a,b):
        if a > b:
            a_points+=1
        elif b > a:
            b_points+=1
        else:
            continue
    print([a_points, b_points])

compareTriplets([6,8,12],[7,9,15])