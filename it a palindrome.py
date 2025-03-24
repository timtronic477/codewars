# Write a function that checks if a given string (case insensitive) is a palindrome.

# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.

def is_palindrome(s):
    lst = list(s.lower())
    mid = len(lst) //2
    if len(lst) == 1: return True
    return lst[:mid] == lst[-mid:][::-1]
