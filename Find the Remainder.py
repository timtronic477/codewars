# Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

# Division by zero should return an empty value.
# Examples:

# n = 17
# m = 5
# result = 2 (remainder of `17 / 5`)

# n = 13
# m = 72
# result = 7 (remainder of `72 / 13`)

# n = 0
# m = -1
# result = 0 (remainder of `0 / -1`)

# n = 0
# m = 1
# result - division by zero (refer to the specifications on how to handle this in your language)
def remainder(a,b):
    if a > b:
        h, l = a, b
    else:
        h, l = b, a
    if l == 0: return None
    return h%l
