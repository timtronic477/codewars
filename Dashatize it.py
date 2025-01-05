# Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

# Ex:

# 274 -> '2-7-4'
# 6815 -> '68-1-5'

def dashatize(n):
    dashes = []
    final = []
    split = list(str(abs(n)))
    for i in split:
        if int(i) % 2 == 0:
            dashes.append(i)
        else:
            dashes.append("-"+i+"-")
    joint = list("".join(dashes))
    for i in range(0, len(joint)):
        
        if joint[i] == "-" and joint[i-1] == "-":
            pass
        else:
            final.append(joint[i])
            
    return "".join(final).strip("-")


# cleaner solution
def dashatize(n):
    if n is None:
        return "None"

    # Convert number to string, handle negatives, and iterate over digits
    digits = str(abs(n))
    result = []

    for i, digit in enumerate(digits):
        if int(digit) % 2 == 0:  # Even number
            result.append(digit)
        else:  # Odd number
            if i > 0 and result[-1] != "-":  # Add a leading dash if needed
                result.append("-")
            result.append(digit)
            result.append("-")  # Always add a trailing dash

    return "".join(result).strip("-")  # Remove leading/trailing dashes
