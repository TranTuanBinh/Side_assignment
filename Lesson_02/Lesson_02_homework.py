#1
'''
Implement the algorithm from description (String: 8-1):
The program asks the user to enter a string. It then uses a for loop to iterate
over the string, counting the number of times that the letter T (uppercase or
lowercase) appears.
'''
# enter a string
str_txt = input('insert your string here:   ')

# for loop
count = 0
for x in str_txt: 
    if x == 't' or x == 'T': 
        count +=1


#2 
password = input('insert your password: ')

correct_length = False
has_uppercase = False 
has_lowercase = False
has_digit = False

if len(password) >= 7:
    correct_length = True

for x in password: 
    if x.isupper(): 
        has_uppercase = True 
    if x.islower(): 
        has_lowercase = True 
    if x.isdigit(): 
        has_digit = True 

if correct_length == has_digit == has_lowercase == has_uppercase == True: 
    is_valid = True 
else: 
    is_valid = False 

print(is_valid)