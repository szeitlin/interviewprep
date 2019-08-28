"""
for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}

have to add a variable to count the swaps
"""
def count_swaps(n:int, a:list):
    """
    number of swaps
    
    :param n: size of the array
    :param a: the array (list of int)
    :return: must print out
    numSwaps
    firstElement
    lastElement
    """
    #these are all placeholders to start
    numSwaps = 0

    for i in range(n):
        for j in range(n-1):
            if a[j]> a[j+1]:
                left = a[j]
                right = a[j+1]
                a[j], a[j+1] = right, left
                numSwaps += 1

    firstElement = a[0]
    lastElement = a[-1]

    print("Array is sorted in {} swaps".format(numSwaps))
    print("First Element: {}".format(firstElement))
    print("Last Element: {}".format(lastElement))

    return (numSwaps,firstElement,lastElement)