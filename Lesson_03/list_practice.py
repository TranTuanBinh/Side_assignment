#1 Create a list named my_list which have items with different datatypes and length at least 5
my_list = ['tuanbinh', 21, 4, 'python', True]
print(my_list)
print('----')
#2 Print all items of my_list 
print(my_list)
print('----')
#3 count the number of each item in my_list 
count = 0 
for i,x in enumerate(my_list):
    if x in my_list: 
        count = count + i 

print(count)

print('----')
#4 Reverse the order of items in my_list 
my_list.reverse()
print(my_list)
print('----')
#5 Square the numberic items in my_list then print result 
for x in my_list: 
    if x is int or x is float: 
        a = x**2
        print(a)
    
print('----')

#6 Add some single values and iterable values  to my_list
#single value: 
my_list.append('thu uyen')
my_list.append(20)
print(my_list)
print('----')
#iterable value: 
my_list.extend(['gia hien', 100, False])

print('----')

#7 Remove values at the end and at the second position of my_list 
my_list.remove(my_list[-1])
my_list.remove(my_list[1])
print('----')
#8 Display those items from my_list that are devisable by 5 
for x in my_list: 
    if x is int or x is float and x % 5 == 0: 
        print(x)
print('----')
#9 Calculate the sum of all numberic items in my_list 
sum = 0
for x in my_list:
    if x is int or x is float: 
        sum = sum + x
        print(sum)
print('----')
#10 Create a new list my_list_str from all string items in my_list then uppercase them 
my_list_str = []
for x in my_list: 
    if x is str: 
        my_list_str.append(x)
print(my_list_str)
print('----')
#11 Create a new list my_list_num from all number items in my_list
my_list_num = []
for x in my_list: 
    if x is int or x is float: 
        
        my_list_num.append(x)

print(my_list_num)
print('----')
#12 Print max/min of my_list_num 
# max
max_num = max(my_list_num)
print(max_num)

#min 
min_num = min(my_list_num)
print(min_num)
print('----')
#13 Remove duplicate value from my_list_num if have 
res =[]
for x in my_list_num: 
    if x not in res: 
        res.append(x)
print('----')
#14 Display odd and even number in my_list_num

# odd number
odd_number =[]
for x in my_list_num: 
    if x % 2 != 0: 
        
        odd_number.append(x)

print(odd_number)

print('----')
# even number
even_number = []
for x in my_list_num: 
    if x % 2 == 0: 
        
        even_number.append(x)

print(even_number)
