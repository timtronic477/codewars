# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Ouput :: "Position of alphabet: 1"



def position(alphabet):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    index = alpha.index(alphabet) + 1
    return f"Position of alphabet: {index}"
