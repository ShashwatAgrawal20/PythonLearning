# its very easy very means very very easy but its bit confusing in starting 

# Difference between 'is' and '=='    {{Important}}

# '==' - Value Equality                         Two objects have the same value 
# 'is' - Reference Equality                     Two references refer to the same object



# >>> a = [3, 5, 32]
# >>> b = a
# >>> b == a
# True
# >>> b is a
# True
# >>> b[0] = 34
# >>> a
# [34, 5, 32]
# >>> c = a[:]
# >>> b == c
# True
# >>> c is a
# False
# >>> c is b
# False
# >>>


# a = [3, 3, "34"]
# b = [3, 3, "34"]

# print(b is a)
# print(b == a)