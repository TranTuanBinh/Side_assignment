#1 create a list named my_list with items which have different datatypes and length at least 5 items
my_list = [123, 234,'hello', False,345] 

#2 print all items of the list in single line
print(my_list) 

#3 count the number of each item in my_list
for x in my_list:
    print(my_list.count(x),x)
#4 reverse the order of the items in my_list
my_list.reverse()   
print(my_list)      

#5 square the numberic items in my_list and print 

for x in my_list:
    if type(x) is int or type(x) is float: 
        print(x**2)

#6 add some single values and iretable value  to my_list
#single value
my_list.append('Tuan Binh')
print(my_list)

#iretable value
my_list.extend(['Tan','Su'])
print(my_list)


#7 remove value at the end and at the second position of my_list
#end 
my_list.pop(-1)
print(my_list)

#second
my_list.pop(1)
print(my_list)

#8 display those items from my_list that are devisible by 5
for x in my_list:
    if type(x) is int  :
        if x % 5 ==0 :
            print(x)

    
#9 calculate the sum of all numberic items in my_list
sum =0
for x in my_list:
    if type(x) is int or type(x) is float :
        sum += x
        print(f'the result is {sum}')

#10 create a new list my_list_str from all string items in my_list then uppercase them
my_list_str =[]
for x in my_list:
    if type(x) is str :
        my_list_str.append(x.upper())
        print(my_list_str)

#11 create a new list my_list_num from all numberic items in my_list
my_list_num = []
for x in my_list:
    if type(x) is int or type(x) is float:
        my_list_num.append(x)
        print(my_list_num)


#12 find max/min value of my_list_num 
#max
max = max(my_list_num)
print(max)

#min
min = min(my_list_num)
print(min)


#13 remove duplicate value from my_list_num, if have 
new_list = []
for x in my_list_num:
    if x not in new_list:
        new_list.append(x) 
        my_list_num = new_list.copy()
        print(my_list_num)

#14 display odd and even number of my_list_num 
for odd in my_list_num:
    if odd % 2 == 0:
        print(odd)

for even in my_list_num:
    if even % 2 != 0:
        print(even)
