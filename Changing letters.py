# When provided with a String, capitalize all vowels

# For example:

# Input : "Hello World!"

# Output : "HEllO WOrld!"

# Note: Y is not a vowel in this kata.

def swap(st):
    vowels = 'aeiou'
    stg = []
    for i in list(st):
        if i in vowels:
            stg.append(i.upper())
        else:
            stg.append(i)
    return "".join(stg)
