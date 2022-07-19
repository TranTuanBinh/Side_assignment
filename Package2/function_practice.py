#1: define a functiobn that accept 2 values and return its sum, subtraction and multiplication (use exception for division)
from audioop import avg
from cmath import sqrt
from itertools import count
from logging import exception


def cal_input(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    try:
        print(a/b)
    except: 
        print('lỗi không thực hiện được')
    
#2: define a function to check whether a number from keyboards is a square number
def square_num_check(a):
    for i in range(a):
        if i * i == a: 
            print('at',i,a,'is a square number')
        else:
            print('at',i,a,'is not a square number')
#3: define a function that accepts 3 arguments then check whether exist a triangle which is crearted by them. Return the result
def func_3(a, b, c):
    if (a > b + c) or (b > a + c) or (c > b + a) :
        print(a,b,c, 'create a triangle')
    else:
        print(a, b, c,'dont create a triangle')


#4 defind a function that accepts one string argument and return number of  vowels and consonants. 
vowel = 0
consonants = 0 
def func_4(message):
    for x in message :
        vowels_List = ('a','e','i','o','u','A','E','I','O','U')
        if x in vowels_List:
            vowel = vowel + 1
        else :
            consonants +=1
print('So luong nguyen am la', vowel)
print('So luong phu am la', consonants)


#5 defind a function that accepts a number (n) and return n first number of Fibonacci sequences


def func_5(n):
    count = 0
    n1, n2 = 0, 1
    if n < 0:
        print('please enter a positive number')
    elif n == 1: 
        print(n1)
    else: 
        print('Fibonacci sequence:')
        while count < n : 
            print(n1)
            nth = n1 + n2 
            n1 = n2 
            n2 = nth 
            count += 1


#6 defind a function that accepts a radius argument and return area and perimeter
def func_6(x): 
    perimeter = 2 * x * 3.14
    print('chu vi hinh tron la', perimeter)
    area = x * x * 3.14
    print('dien tich hinh tron la', area)

#7 defind a function that accepts 2 arguments: first argument is a list of interger, second argument is a number with default value is 3 
#repeat the list by the number, then calculate average of all items in the list
def func_7(list_num_arg, num_arg = 3):
    new_res = list_num_arg * num_arg
    print(new_res)
    avg_new_res = sum(new_res) / len(new_res)
    print('average of new list =', avg_new_res)








