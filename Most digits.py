# Find the number with the most digits.

# If two numbers in the argument array have the same number of digits, return the first one in the array.

def find_longest(arr):
    longest = 0
    for i in arr:
        if len(list(str(i))) > len(list(str(longest))):
            longest = i
    return longest
