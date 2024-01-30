"""String Functions
Capitalise()->1st char string change to capital
UpperCase()->All string convert to Capital
LowerCase()->All string convert to lower case
SwapCase()->In i/p If UP it convert to LP, If LP convert to UP
"""
name=input("Enter your Name:")
result1=print(name.capitalize())
result2=print(name.upper())
result3=print(len(name))
result4=print(name.lower())

name="sOWJANYA"
print(name.swapcase())

#slicing
text="hello world"
print(text[0],text[4])

#find
print(text.find('hello')) #Check the index of hello


#count() count the char
count=text.count("l")
print(count)


