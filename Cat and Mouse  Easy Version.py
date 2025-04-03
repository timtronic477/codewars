# You will be given a string featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'. The string will start with the cat, and end with the mouse.

# You need to find out if the cat can catch the mouse from its current position. The cat can jump over at most three characters. So:

# "C.....m" returns "Escaped!" <-- more than three characters between

# "C...m" returns "Caught!" <-- as there are three characters between the two, the cat can jump.
def cat_mouse(x):
    count = 0
    for i in range(1, len(x)):
        if x[i] == ".":
            count +=1 
    return "Escaped!" if count > 3 else "Caught!"
