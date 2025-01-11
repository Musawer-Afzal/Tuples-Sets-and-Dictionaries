# Write a program to Check if a given string is binary string of or not.
# A string is said to be binary if it's consists of only two unique characters.
# Take string input from user.
# Input: str = "01010101010"
# Output: Yes
# Input: str = "1222211"
# Output: Yes
# Input: str = "Campusx"
# Output: No

string = input("Enter a string: ")
unique_char = set(string)

if len(unique_char) == 2:
    print("Yes")
else:
    print("No")
