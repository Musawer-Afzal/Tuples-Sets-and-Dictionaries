# Convert a list of Tuples into Dictionary.
# Example 1:
# Input:
# [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# Output:
# {'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
# Example 2:
# Input:
# [('A', 1), ('B', 2), ('C', 3)]
# Output:
# {'A': [1], 'B': [2], 'C': [3]}


tpl1 = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
tpl1 = dict(tpl1)

for key in tpl1:
    tpl1[key] = [tpl1[key]]

print(tpl1)