#1 assign a string to a variable named str_txt and display
str_txt = 'hello every one im binh'

print(str_txt)
#2 string as array: display some characters of str_txt:
# - 3 first characters 
str_txt[:2]

# -  4 last characters 
str_txt[-4:]
# - characters from position 1 to 4 
str_txt[1:4]
# - character from first position to 5
str_txt[:5]
#3 loop through string 
#print all characters of str_txt, using for loop iretation 
for char in str_txt: 
    print(char)

#4 print length of string str_txt 
print(len(str_txt))
#5 check if str_txt containt other string. If has, print start position of that string
substring = 'binh'

if substring in str_txt: 
    print(str_txt.index(substring[0]))


#6 print str_txt with all characters are upper/lower
#upper
print(str_txt.upper())

#lower
print(str_txt.lower())

#print str_txt with all first characters of each words are upper
print(str_txt.capitalize())

#7 remove all white space 
''.join(str_txt.split())

#8 replace all h character with m character
print(str_txt.replace('h','m'))

#9 split str_txt by whitespace and display second item of array 
print(str_txt.split(' '))
print(str_txt[1])