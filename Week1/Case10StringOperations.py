# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String:") 
print(text.title())

# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize())

# original string never changes
print("\nOriginal String")
print(text)

# slice,breaking the string
st = "WsCubeTech"  #
print(st[::])      #WsCubeTech
print(st[0::])     #WsCubeTech
print(st[0::1])    #WsCubeTech
print(st[6::])     #Tech
print(st[0:6:])    #WsCube
print(st[::-1])    #hceTebuCsW
print(st[-3::-1])  #eTebuCsW
print(st[2:5:])    #Cub


st = "WsCubeTech" # len fn is used to describe the lenghth of variable 
n = len(st)
print(n)


st = "WsCubeTech" # right to left scanning  or if +1 is used to scan from left to right 
rev_st = st[::-1]
print(rev_st)


for i in "WsCubeTech":
   # if(i--2) we can add conddition but this is for loof for string
    print(i)