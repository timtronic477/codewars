# Implement a function that takes two numbers m and n and returns an array of the first m multiples of the real number n. Assume that m is a positive integer.

# Ex.

# (3, 5.0) --> [5.0, 10.0, 15.0]

def multiples(m, n):
    return [n*i for i in range(1, m+1)]
