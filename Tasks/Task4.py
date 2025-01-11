# Count no of tuples, list and set from a list
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
# Output:
# List-2
# Set-2
# Tuples-1


list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

dic = {}
count = 0
for i in list1:
    if type(i) == list:
        # Using defalult value 0, since List in dictionary is empty
        dic["List"] = dic.get("List", 0) + 1
    elif type(i) == tuple:
        dic["Tuple"] = dic.get("Tuple", 0) + 1
    elif type(i) == set:
        dic["Set"] = dic.get("Set", 0) + 1
for i in dic:
    print(i,"-", dic[i])