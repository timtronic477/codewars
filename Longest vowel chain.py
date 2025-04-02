# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou. 

def solve(s):
    vowels = 'aeiou'
    max_ = 0
    count = 0
    for i in s:
        if i in vowels:
            count += 1
            max_ = max(max_, count)
        else:
            count = 0
    return max_
        
