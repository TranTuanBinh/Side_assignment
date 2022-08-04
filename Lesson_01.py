from tkinter import Y
from unicodedata import name


print('hello world')


while True:
    response = input()
    if int(response) % 7 == 0:
        print('the input number is', f'{response}')


cities = ['hcm', 'hue', 'hanoi']
for i,city in enumerate(cities): 
    print(i,city)

list_1 = [1,3,4,5,7,8]
list_2 = [3,6,8,9,1,3]

for x, y in zip(list_1, list_2): 
    print(x,y)


for i,x in enumerate(range(1,1001)):
    print(i,'lets learn how to develope your future')