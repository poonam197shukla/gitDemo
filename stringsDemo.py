#strings
#string is actually a list in Python

str1 ="poonam197shukla@gmail.com"
str2="This is my email"
str3="poonam"

print(str1[0])

print(str1[0:6])

#concatenation in strings
print(str1+str2)

#to check if one string is present in another string or not(substring)
print(str3 in str1)

#splitting of string
var=str1.split(".")
print(var)
print(var[0])

#to remove white spaces from string
str4="   great   "
#print(str4.strip())

#to remove only left side white spaces
#print(str4.lstrip())

#to remove only left side white spaces
print(str4.rstrip())


