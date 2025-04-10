# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

# The result should also be ordered from highest to lowest.

# Examples:

# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []

def two_highest(arg1):
    lst = list(reversed(sorted(arg1)))
    val = []
    for i in range(0, len(lst)):
        if lst[i] not in val:
            val.append(lst[i])
    return val[:2]
