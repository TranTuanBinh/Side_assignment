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
    if type(a.sqrt) is int:
        print(a,'is a square number')
    else :
        print(a,'is not a square number')

#3: define a function that accepts 3 arguments then check whether exist a triangle which is crearted by them. Return the result
def func_3(x1, y1, x2, y2, x3, y3):
    a =  (x1 * (y2 - y3) +
         x2 * (y3 - y1) +
         x3 * (y1 - y2))

    if a == 0:
        print('No')
    else:
        print('Yes')


#4 defind a function that accepts one string argument and return number of  vowels and consonants. 
count = 0
def func_4(message):
    for x in message:
        if x == 'a'and x == 'e' and x == 'i' and x == 'o' and x == 'u':
            count = count +1
        else :
            count = count +1


#5 defind a function that accepts a number (n) and return n first number of Fibonacci sequences



#6 defind a function that accepts a radius argument and return area and perimeter
def func_6(x): 
    perimeter = 2 * x * 3.14
    print('chu vi hinh tron la', perimeter)
    area = x * x * 3.14
    print('dien tich hinh tron la', area)

#7 defind a function that accepts 2 arguments: first argument is a list of interger, second argument is a number with default value is 3 
#repeat the list by the number, then calculate average of all items in the list
def func_7(first_arg, second_arg = 3):
    new_res = first_arg * second_arg
    print(new_res)
    avg_new_res = sum(new_res) / len(new_res)
    print('average of new list =', avg_new_res)


