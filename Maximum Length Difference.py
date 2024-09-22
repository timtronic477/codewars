# You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

# Find max(abs(length(x) − length(y)))

# If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).
# Example:

# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(a1, a2) --> 13

def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    a1_max = max(a1, key=len)
    a2_max = max(a2, key=len)
    a1_min = min(a1, key=len)
    a2_min = min(a2, key=len)
    b = abs(len(a1_max)-len(a2_min))
    c = abs(len(a2_max)-len(a1_min))
    
    return b if b>c else c


