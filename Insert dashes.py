# Write a function that takes an integer num (num >= 0) and inserts dashes ('-') between each two odd digits in num.
# Examples

# 454793 ---> "4547-9-3"
#      0 ---> "0"
#      1 ---> "1"
# 13579  ---> "1-3-5-7-9"
#  86420 ---> "86420"

def insert_dash(num):
    splt = list(str(num))
    arr = [splt[0]]
    for i in range(1, len(splt)):
        if int(splt[i])%2 == 1 and int(splt[i-1])%2==1:
            arr.append("-")
        arr.append(splt[i])
    return "".join(arr)
