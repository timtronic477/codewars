# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

# Example:

# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):
    letters = {
        "a":"b",
        "b":"a",
        "c":"c"
    }
    phrase = ""
    for i in list(s):
        phrase += letters[i]
    return phrase
