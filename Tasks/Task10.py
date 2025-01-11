# Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.
# Example 1:
# Input:
# lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
# lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
# Output:
# [9, 10, 4, 5]
# Example 2:
# Input:
# lst1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}
# lst2 = {9, 9, 74, 21, 45, 11, 63, 28, 26}
# Output:
# [9, 11, 26, 28]


lst1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}
lst2 = {9, 9, 74, 21, 45, 11, 63, 28, 26}

result1 = [i for i in lst1 if i in lst2]
print(sorted(result1))

lst3 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst4 = {9, 4, 5, 36, 47, 26, 10, 45, 87}

result2 = [i for i in lst3 if i in lst4]
print(sorted(result2))