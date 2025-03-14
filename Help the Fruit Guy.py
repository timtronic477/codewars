# Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. He wants to replace all the rotten pieces of fruit with fresh ones. For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"]. Your task is to implement a method that accepts an array of strings containing fruits should returns an array of strings where all the rotten fruits are replaced by good ones.
# Notes

#     If the array is null/nil/None or empty you should return empty array ([]).
#     The rotten fruit name will be in this camelcase (rottenFruit).
#     The returned array should be in lowercase.

def remove_rotten(bag_of_fruits):
    new_fruit = []
    for i in bag_of_fruits:
        if i[:6] == 'rotten':
            new_fruit.append((i[6:]).lower())
        else:
            new_fruit.append(i)
    return new_fruit
