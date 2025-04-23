# Write a function that removes every lone 9 that is inbetween 7s.

# "79712312" --> "7712312"
# "79797"    --> "777"

def seven_ate9(str_):
    s = list(str_)
    f = []
    for i in range(0, len(s)):
        if s[i] != "9":
            f.append(s[i])
        else:
            if i != 0 and i != (len(s)-1):
                if s[i-1] =="7"and s[i+1] == "7":
                    pass
                else:
                    f.append(s[i])
            else:
                f.append(s[i])
    return "".join(f)


while "797" in str_:
  str_ = str_.replace("797", "77")
return str_
