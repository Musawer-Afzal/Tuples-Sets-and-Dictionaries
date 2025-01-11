# Join Tuples if similar initial element
# While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.
# For eg.
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)


# Initialize the test list
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

# Initialize an empty dictionary to group elements
grouped = {}

# Iterate through the list of tuples
for tpl in test_list:
    key = tpl[0]
    if key not in grouped:
        grouped[key] = list(tpl[1:])
    else:
        grouped[key].extend(tpl[1:])

# Create the resulting list by concatenating elements
result = [tuple([key] + grouped[key]) for key in grouped]

# Print the result
print(result)