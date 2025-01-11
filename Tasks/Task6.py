# Write a program to find set of common elements in three lists using sets.
# Input : ar1 = [1, 5, 10, 20, 40, 80]
#         ar2 = [6, 7, 20, 80, 100]
#         ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Output : [80, 20]

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

result = set(ar1) & set(ar2) & set(ar3)
print(list(result))