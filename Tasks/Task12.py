# Replace words from Dictionary. Given String, replace it’s words from lookup dictionary.
# Example 1:
# Input:
# test_str = 'CampusX best for DS students.'
# repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
# Output:
# CampusX is the best channel for Data-Science students.
# Example 2:
# Input:
# test_str = 'CampusX best for DS students.'
# repl_dict = {"good" : "is the best channel", "ds" : "Data-Science"}
# Output:
# CampusX best for DS students.


test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

for key in repl_dict:
    test_str = test_str.replace(key, repl_dict[key]) 

print(test_str)