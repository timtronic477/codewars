# Definition

# A Tidy Number is a number whose digits are in non-decreasing order.
# Task

# Given a number, determine if it is tidy or not.

def tidyNumber(n):
    for i in range(1, len(list(str(n)))):
        if int(list(str(n))[i]) < int(list(str(n))[i-1]):
            return False
    return True
