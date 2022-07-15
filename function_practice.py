#1: define a functiobn that accept 2 values and return its sum, subtraction and multiplication (use exeption for division)
from audioop import avg
from cmath import sqrt
from itertools import count


def cal_input(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    try: 
        print(a/b)
    except:
        print('lỗi')
        raise
    finally :
        print(a/b)
#2: define a function to check whether a number from keyboards is a square number
def square_num_check(a):

    if type(sqrt(a)) is int:
        print(a,'is a square number')
    else :
        print(a,'is not a square number')

#3: define a function that accepts 3 arguments then check whether exist a triangle which is crearted by them. Return the result
def func_3(a, b, c):
    if (a > b + c) or (b > a + c) or (c > b + a) :
        print(a,b,c, 'create a triangle')
    else:
        print(a, b, c,'dont create a triangle')


#4 defind a function that accepts one string argument and return number of  vowels and consonants. 
count_1 = 0
count_2 = 0
def func_4(message):
    for x in message:
        if x == 'a'or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            count_1 = count_1 +1
        else :
            count_2 = count_2 +1

    print('so nguyen am la', count_1)
    print('so phu am la', count_2)


#5 defind a function that accepts a number (n) and return n first number of Fibonacci sequences



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

