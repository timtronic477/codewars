# Modify the kebabize function so that it converts a camel case string into a kebab case.

# "camelsHaveThreeHumps"  -->  "camels-have-three-humps"
# "camelsHave3Humps"  -->  "camels-have-humps"
# "CAMEL"  -->  "c-a-m-e-l"

# Notes:

#     the returned string should only contain lowercase letters

# Modify the kebabize function so that it converts a camel case string into a kebab case.

# "camelsHaveThreeHumps"  -->  "camels-have-three-humps"
# "camelsHave3Humps"  -->  "camels-have-humps"
# "CAMEL"  -->  "c-a-m-e-l"

# Notes:

#     the returned string should only contain lowercase letters

def kebabize(st):
    words = []
    current = ''
    
    for i in st:
        if i.isdigit():
            continue
        elif i.isupper() and current:
            words.append(current)
            current = i.lower()
        else:
            current += i.lower()
    words.append(current)
    return "-".join(words)
            
