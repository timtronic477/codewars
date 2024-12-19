# In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters (everything else), as follows.

# The order is: uppercase letters, lowercase letters, numbers and special characters.

# "*'&ABCDabcde12345" --> [ 4, 5, 5, 3 ]

# More examples in the test cases.

# Good luck!

def solve(s):
    upper = 0
    lower = 0
    num = 0
    rand = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isnumeric():
            num += 1
        else:
            rand += 1
    return [upper, lower, num, rand]
    
