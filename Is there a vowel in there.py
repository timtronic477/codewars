# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

# If they are, change the array value to a string of that vowel.

# Return the resulting array.

def is_vow(inp):
    vowel_codes = {
    97: 'a',
    101: 'e',
    105: 'i',
    111: 'o',
    117: 'u'
}
    new_arr = []
    for i in inp:
        if i in vowel_codes:
            new_arr.append(vowel_codes[i])
        else:
            new_arr.append(i)
    return new_arr
