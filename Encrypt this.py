# Description:
# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
    words = text.split(" ")
    new_words = []
    if len(text) == 0: return ""
    for word in words:
        if len(word) == 1:
            new_words.append(str(ord(word)))
        elif len(word) == 2:
            new_words.append(str(ord(word[0])) + word[1])
        else:
            new_word = str(ord(word[0])) + word[len(word) - 1] + word[2:len(word) - 1] + word[1]
            new_words.append(new_word)
    return " ".join(new_words)
