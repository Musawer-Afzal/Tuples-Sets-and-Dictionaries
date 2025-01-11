# Join Tuples if similar initial element
# While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.
# For eg.
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)


test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

result = []
for i in range(len(test_list)):
    if test_list[i][0]  == test_list[i+1][0]:
        result.append((test_list[i][0], test_list[i][1], test_list[i+1][1]))

print(result)