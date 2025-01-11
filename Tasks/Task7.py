# Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
# Input:
# Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
# Output:
# No of unique vowels-6


Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

vowels = set("aeiouAEIOU")
unique_Vowels = 0
arr_vowels = []

for char in Str1:
    if char in vowels and char not in arr_vowels:
        arr_vowels.append(char)
        unique_Vowels += 1

print("No of unique vowels-", unique_Vowels)