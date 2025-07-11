# Compare two strings by comparing the sum of their values (ASCII character code).

#     For comparing treat all letters as UpperCase
#     null/NULL/Nil/None should be treated as empty strings
#     If the string contains other characters than letters, treat the whole string as it would be empty

# Your method should return true, if the strings are equal and false if they are not equal.
# Examples:

# "AD", "BC"  -> equal
# "AD", "DD"  -> not equal
# "gf", "FG"  -> equal
# "zz1", ""   -> equal (both are considered empty)
# "ZzZz", "ffPFF" -> equal
# "kl", "lz"  -> not equal
# null, ""    -> equal

def compare(s1, s2):
    val1 = 0
    val2 = 0
    if s1 != None:
        if s1.isalpha():
            val1 = sum([ord(i) for i in list(s1.upper())])
    if s2 != None:
        if s2.isalpha():
            val2 = sum([ord(i) for i in list(s2.upper())])
    return val1 == val2
