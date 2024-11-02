# Write a small function that returns the values of an array that are not odd.

# All values in the array will be integers. Return the good values in the order they are given.

def no_odds(values):
    lst = []
    for i in values:
        if i == 0 or i%2 == 0:
            lst.append(i)
    return lst
    
