# Write a function that takes an array of unique integers and returns the minimum number of integers needed to make the values of the array consecutive from the lowest number to the highest number.
# Example

# [4, 8, 6] --> 2
# Because 5 and 7 need to be added to have [4, 5, 6, 7, 8]

# [-1, -5] --> 3
# Because -2, -3, -4 need to be added to have [-5, -4, -3, -2, -1]

# [1] --> 0
# []  --> 0


def consecutive(arr):
    l = len(arr)
    c = 0
    s = sorted(arr)
    if l <=1:
        return 0
    for i in range(s[0], s[l-1]):
        c += 1
    return c-l+1
