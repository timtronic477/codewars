# Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable examples from the film Hackers.

# Your task is to create a function that, given a proper first and last name, will return the correct alias.
# Notes:

#     Two objects that return a one word name in response to the first letter of the first name and one for the first letter of the surname are already given. See the examples below for further details.

#     If the first character of either of the names given to the function is not a letter from A - Z, you should return "Your name must start with a letter from A - Z."

#     Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for these grammatical errors.

# Examples

# # These two dictionaries are preloaded, you need to use them in your code
# FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
# SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}

# alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
# alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'

# Happy hacking!

def alias_gen(f_name, l_name):
    fname_letter = f_name[0]
    lname_letter = l_name[0]
    if fname_letter.upper() not in FIRST_NAME or lname_letter.upper() not in SURNAME:
        return 'Your name must start with a letter from A - Z.'
    else:
        return f'{FIRST_NAME[fname_letter.upper()]} {SURNAME[lname_letter.upper()]}'
