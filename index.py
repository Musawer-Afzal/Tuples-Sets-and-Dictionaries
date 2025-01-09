                        # TUPLES
# Creating Tuples
t1 = ()
print(t1) # ()
#Create a tuple with one item
# Hmmpgeneous Tuple
t2 = (2)
print(type(t2)) # <class 'int'>
t3 = ('hello')
print(t3) # <class 'string'>
# heterogenoues tuple
t4 = (1,2,3, True,[1,2,3])
print(t4) # (1, 2, 3, True, [1, 2, 3])
# Nested tuple
t5 = (1,2,3,(5,6))
print(t5)
# Using type Conversion
t6 = tuple([1,2,3])
t7 = tuple("Hello")
print(t6) # (1, 2, 3)
print(t7) # ('H', 'e', 'l', 'l', 'o')


# Accessing Items from a Tuple
t = (1,2,3,4,5)
print(t[0]) # 1
print(t[-1]) # 5
# Slicing
print(t[0:3]) # (1, 2, 3)
# Negative Indexing
print(t[-3:]) # (4, 5)
print(t[::2]) # (1, 3, 5)
print(t[::-1]) # (5, 4, 3, 2, 1)
# Accessing Nested tuple
print(t5[3][1]) # 6
print(t5[-1][0]) # 5


# Modifying Tuples
# Immutable
t = (1,2,3)
# t[0] = 100 # This will give an error

# Adding Items
t = (1,2,3)
t = t + (4,5,6)
print(t) # (1, 2, 3, 4, 5, 6)
# Removing Items
t = (1,2,3,4,5)
t = t[:2] + t[3:]
print(t) # (1, 2, 4, 5)


# Deleting Items, You can only delete whole Tuples
t = (1,2,3,4,5, "Hello")
print(t)
del t
# print(t) # This will give an error


# Operations on Tuples
# + and *
t1 = (1,2,3)
t2 = (4,5,6)
print(t1 + t2) # (1, 2, 3, 4, 5, 6)
print(t1 * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# Membership
print(2 in t1) # True
print(2 not in t1) # False
# Iteration
for i in t1:
    print(i)


# Tuple Functions
# len/sum/min/max/sorted/count/index
t = (1,2,3,4,5)
print(len(t)) # 5
print(sum(t)) # 15
print(min(t)) # 1
print(max(t)) # 5
print(sorted(t)) # [1, 2, 3, 4, 5]
print(sorted(t, reverse = True)) # [5, 4, 3, 2, 1]
print(t.count(5)) # 1
print(t.index(5)) # 4

# Special syntax
# Tuple Unpacking
a,b,c = (1,2,3)
print(a) # 1
print(b) # 2
print(c) # 3

# Swapping
a = 1
b = 2
a,b = b,a
print(a,b) # 2 1

# a,b = (1,2,3,4)
#print(a,b) # Will throw an error
a,b,*other = (1,2,3,4)
print(a,b)
print(other) # Will store the rest of values in a list


# Zipping Tuples
a = (1,2,3,4)
b = (5,6,7,8)
print(zip(a,b)) # <zip object at 0x0000026DD0E47340>, It will make a zip object
print(list(zip(a,b)))
print(tuple(zip(a,b)))



                                # SETS



# Creating Sets
# Empty Set
s = {}
print(s) # {}
print(type(s)) # dict, Dictionary and set have same syntax. Default method is given to dictionary
# How to actually declare a set?
s = set()
print(type(s)) # set
# Homogeneous Set
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {3, 4, 5, 6, 7}

# Sets are Immutable
# s = {1,2,3,4,5,{5,6,7}} # Will throw and error since Mutable items connot be in a set

# Heterogeneous Set
s3 = {1,2,3,"Hello", True,(1,2,3)}
print(s3) # {1, 2, 3, 'Hello'}, Won't give True since True is same as 1. And Sets can't have duplicate values

# Using type Conversion
s3 = set([1,2,3,4,5])
s4 = set("Hello")
print(s3) # {1, 2, 3, 4, 5}
print(s4) # {'H', 'e', 'l', 'o'}



# Accessing Sets, You can't access items in Sets
s = {1,2,3,4,5}
# print(s[0]) # Will throw an error since Sets are Immutable
# print(s[1:3]) # Will throw an error since Sets are Immutable

# Edit item in Sets, This is also not allowed
s1 = {1,2,3,4,5}
# s1[0] = 100 # Will throw an error since Sets are Immutable
# print(s1)


# Adding Items
# add, to add one item at a time
s1 = {1,2,3,4,5}
s1.add(6)
print(s1) # {1, 2, 3, 4, 5, 6}
# update, to add multiple items at a time
s1 = {1,2,3,4,5}
s1.update([6,7,8])
print(s1) # {1, 2, 3, 4, 5, 6, 7, 8}
s1.update((9,10,11))
print(s1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
s1.update({12,13,14})
print(s1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

# Deleting Items
s1 = {1,2,3,4,5}
print(s1, "First s")
# del s1[0]
print(s1) # Will throw an error since s1 is Immutable
# remove, to remove one item at a time
s1 = {1,2,3,4,5}
s1.remove(3)
print(s1) # {1, 2, 4, 5}
#s1.remove(45) # It will throw an error
print(s1) 
# discard, to remove one item at a time
s1 = {1,2,3,4,5}
s1.discard(3)
print(s1) # {1, 2, 4, 5}
s1.discard(4546)
print(s1) # It will not throw an error
# pop
s1 = {1,2,3,4,5}
s1.pop() # It will randomly delete an item
print(s1) # {2, 3, 4, 5}
# clear, to remove all items at a time
s1 = {1,2,3,4,5}
s1.clear()
print(s1) # set()


# Set Operations
# Union
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1 | s2) # Every item(No Duplicate) will be printed
# Intersection
print(s1 & s2) # Common Items from both sets will be printed
# Difference
print(s1 - s2) # Items in s1, that are not present in s2, will be printed. 1,2,3
# Symmetric Difference(^)
print(s1 ^ s2) # Every items, other than common, will be printed
# Membership Test
print(1 in s1)
print(1 not in s1)
# Iteration
for i in s1:
    print(i)


# FUNCTIONS
# len/sum/min/max/sorted
s = {3,1,4,5,2,7}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s)) # Sorted result is always in list
# Union/Update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2), "Union")
s1.update(s2)
print(s1)
print(s2)
s2.update(s1)
print(s1)
print(s2)
# Intersection/Intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.intersection(s2), "Intersection")
print(s2)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.intersection_update(s2)
print(s1, "Intersection_update")
# Difference/Difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.difference(s2), "Difference")
s1.difference_update(s2)
print(s1)
# Symmetric Difference
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.symmetric_difference(s2), "Symmetric_Difference")
s1.symmetric_difference_update(s2)
print(s1)
# Membership Test
s1 = {1,2,3,4,5}
print(1 in s1)
print(1 not in s1)

# isdisjoint/issubset/issuperset/copy
# isdisjoint, The sets that do not have anything in common
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.isdisjoint(s2)), # will give False since they have common items
# issubset
s1 = {1,2,3,4,5}
s2 = {3,4,5}
print(s1.issubset(s2)), # will give False since s2 contain elements present in s1, hence s2 is subset of s1.
# issuperset
s1 = {1,2,3,4,5}
s2 = {3,4,5}
print(s1.issuperset(s2)), # will give true since s1 is a superset of s2.
# copy
s1 = {1,2,3,4,5}
s2 = s1.copy()
print(s1)
print(s2)

# Frozen set, It is an Immutable version of Python Set
fs1 = frozenset([1,2,3,4,5])
print(fs1)
fs2 = frozenset([3,4,5,6,7])
print(fs2)
print(fs1.union(fs2))

# 2D Sets
fs = frozenset([1,2,frozenset([3,4,5])])
print(fs)

# Set Comprehension
s = {x for x in range(1,11) if x % 2 == 0}
print(s)





#                           DICTIONARIES

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and they have keys and values.
# Keys are unique, and must be of any hashable type.

# Characteristics
# 1. Mutable
# 2. Indexing has no meaning
# 3. Keys can't be duplicated
# 4. Keys can't be mutable items

# dict = {"name": "John", "age": 36, "country": "Norway", "gender": "Male"}


# Creating Dictionaries
# 1. Empty Dictionary
d = {}
print(d) # {}
# 2. 1D Dictionary/Dictionary with keys and values
d = {"name": "John", "age": 36, "country": "Norway", "gender": "Male"}
print(d) # {'name': 'John', 'age': 36, 'country': 'Norway', 'gender': 'Mnale'}
# 3. 2D Dictionary
s = {
    "name": "Harry Potter",
    "college": "Daffodil International University",
    "semester": 4,
    "subjects":{
        "dsa": 50,
        "oop": 80,
        "english": 60
    }
}
print(s)

# using Sequence and dict function
d4 = dict([(1,2), (3,4), (5,6)])
print(d4) # {1: 2, 3: 4, 5: 6}
d4 = dict([("name","Hermione"), ("age",34), (5,6)])
print(d4)

# Duplicate Keys, They are not allowed
d5 = {"name": "harry", "name": "Hermione"}
print(d5) # The last updated value will be printed

# Mutable Items as keys
# d6 = {"name": "harry", [1,2,3]: 2} # It will throw an error, List cannot be used as a key
d6 = {"name": "harry", "list":[1,2,3]}
print(d6)


# Accessing Items
# 1st method
my_dict= {"name": "jack", "age": 23}
print(my_dict["name"]) # jack
print(my_dict["age"]) # 23
# 2nd Method
print(my_dict.get("name")) # jack
print(my_dict.get("age")) # 23


# Adding New Value key-pair
d5 = {"name": "harry", "gender": "Male"}
d5["name"] = "Marshal"
print(d5)
d5["weight"] = 60
print(d5)


# Remove Key-value pair
# pop, To remoove a particular Key-value
d4 = {"name": "John", "age": 36, "country": "Norway", "gender": "Male"}
d4.pop("country")
print(d4) # {'name': 'John', 'age': 36, 'gender': 'Male'}
# popitem, Remove the last item in the dictioinary
d4 = {"name": "John", "age": 36, "country": "Norway", "gender": "Male"}
d4.popitem()
print(d4)
# del, Delete the entire dictionary or specific key-value pair
# It works the same as pop
d4 = {"name": "John", "age": 36, "country": "Norway", "gender": "Male"}
del d4["name"]
print(d4)
# clear, Gives an empty dictionary
d4 = {"name": "John", "age": 36, "country": "Norway", "gender": "Male"}
d4.clear()
print(d4)

# using 2D
s = {
    "name": "Harry Potter",
    "college": "Daffodil International University",
    "semester": 4,
    "subjects":{
        "dsa": 50,
        "oop": 80,
        "english": 60
    }
}
print(s["subjects"]["oop"])
print(s.get("subjects").get("oop"))
s["subjects"]["calculus"] = 87
print(s)
# Remove key-value pair
del s["subjects"]["calculus"]
print(s)
# s.popitem()
# print(s)


# Editing key-value pair
s = {
    "name": "Harry Potter",
    "college": "Daffodil International University",
    "semester": 4,
    "subjects":{
        "dsa": 50,
        "oop": 80,
        "english": 60
    }
}
s["semester"] = 5
print(s)
s["subjects"]["oop"] = 90
print(s)



# Dictionary Operations
# Membership
s = {
    "name": "Harry Potter",
    "college": "Daffodil International University",
    "semester": 4,
    "subjects":{
        "dsa": 50,
        "oop": 80,
        "english": 60
    }
}
print("name" in s) # True
print("Harry Potter" in s) # False

# Iteration
d = {"name": "Nitish", "gender": "Male", "age": 23}
for i in d:
    print(i, d[i]) # to print key-value pair together



# Dictionary Functions
# len
d = {"name": "Nitish", "gender": "Male", "age": 23}
print(len(d))
# sorted
print(sorted(d))
print(sorted(d,reverse = True))

# max, min
d = {"name": "Nitish", "gender": "Male", "age": 23}
print(max(d)) # age
print(min(d)) # name

# items/keys/values
# Items, it displays all the key-value pair in the form of Tuples
d = {"name": "Nitish", "gender": "Male", "age": 23}
print(d.items())
# Keys, Give all the keys in the form of list
d = {"name": "Nitish", "gender": "Male", "age": 23}
print(d.keys())
# Values, Give all the values in the form of list
d = {"name": "Nitish", "gender": "Male", "age": 23}
print(d.values())
# update
d1 = {1:2, 3:4, 4:5}
d2 = {4:7, 6:8}
d1.update(d2)
print(d1)



# Dictionary Comprehension
d = {x:x**2 for x in range(1,11)}
print(d)
distances = {"delhi": 1000, "mumbai": 2000, "bangalore": 3000}
d_comprehension = {key: values*0.62 for (key, values) in distances.items()}
print(d_comprehension)

# zip
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_C = [10, 20, 30, 40, 50, 60, 70]
d_comprehension = {i:j for (i,j) in zip(days, temp_C)}
print(d_comprehension)

products = {"phone": 10, "laptop": 0, "charger": 32, "Tablet": 0}
products_comprehension = {key:values for (key, values) in products.items() if values > 0}
print(products_comprehension)

# Nested Comprehensiom
# print a table of 2,3,4 upto 10
tables = {i:{j:i*j for j in range(1,11)} for i in range(2,5)}
print(tables)