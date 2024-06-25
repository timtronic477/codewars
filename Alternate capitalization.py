# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

def capitalize(s):
    word1 = ""
    word2 = ''
    for i in range(0, len(s)):
        if i%2==0:
            word1 += s[i].upper()
        else:
            word1 += s[i]
            
    for i in range(0, len(s)):
        if i%2==0:
            word2 += s[i]
        else:
            word2 += s[i].upper()
    return [word1, word2]
