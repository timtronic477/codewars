# Your task is to write function factorial.

# https://en.wikipedia.org/wiki/Factorial

def factorial(n):
    if n == 0: return 1
    total = n
    sub_value = n - 1
    while sub_value > 0:
        total *= sub_value
        sub_value -= 1
    return total
