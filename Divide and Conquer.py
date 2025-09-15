# Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

# Return as a number.

def div_con(x):
    nums = 0
    strs = 0
    for i in x:
        if type(i) == str:
            strs += int(i)
        else:
            nums += i
    return nums - strs
