# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(s):
    index = len(s)
    for i in range(len(s) -1, -1, -1):
        if not s[i].isdigit():
            index = i + 1
            break
        
    word, num = s[:index], s[index:]
    if s == "": return "1"
    if len(num) == 0:
        if word[0].isalpha():
            return word + "1"
        else:
            return str(int(word) + 1).zfill(len(word))
    else: 
        converted_num = str(int(num) + 1).zfill(len(num))
        return word + converted_num
