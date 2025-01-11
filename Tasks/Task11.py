# Key with maximum unique values
# Given a dictionary with values list, extract key whose value has most unique values.
# Example 1:
# Input:
# test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
# Output:
# CampusX
# Example 2:
# Input:
# test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# Output:
# Best


test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
max_unique_value = 0

for key in test_dict:
    unique_values = len(set(test_dict[key]))
    if unique_values > max_unique_value:
        max_unique_value = unique_values
        max_unique_key = key

print(max_unique_key)


test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
max_unique_value = 0

for key in test_dict:
    unique_values = len(set(test_dict[key]))
    if unique_values > max_unique_value:
        max_unique_value = unique_values
        max_unique_key = key

print(max_unique_key)