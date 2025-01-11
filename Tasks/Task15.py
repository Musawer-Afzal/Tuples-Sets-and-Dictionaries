# Sort Dictionary key and values List.
# Example 1:
# Input:
# {'c': [3], 'b': [12, 10], 'a': [19, 4]}
# Output:
# {'a': [4, 19], 'b': [10, 12], 'c': [3]}
# Example 2:
# Input:
# {'c': [10, 34, 3]}
# Output:
# {'c': [3, 10, 34]}



dict1 = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

result = sorted(dict1.items())
print(result)