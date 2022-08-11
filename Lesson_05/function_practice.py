#1 define a function that accept 2 values and return their sum, division subtraction and multiplication. (use exception for division)
import math


def cal(num1, num2): 
    print('the result of sum is:', num1 + num2)
    print('the result of subtraction is:', num1 - num2)
    print('the result of multiplication is:', num1 * num2 )
    try: 
        print('the result of division is:', num1 / num2)
    except: 
        print('cannot devide by 0')
    


#2 define a function to check whether a number from keyboard is a square number.
def square_check():
    number = int(input('Enter your number:  '))
    sqrtnum = int(math.sqrt(number))
    return sqrtnum * sqrtnum == number


#3 define a function accept 3 arguments, then check whether exist a triangle which created by them 
def triangle_check(x,y,z):
    if (x+y)> z or (x + z)>y or (y+z)>x:
        print(x,y,z,'can create a triangle')
    else:
        print(x,y,z,'cannot create a triangle')



#4 define a function that accept one string argument and return number of vowels and consonants
def str_cal(string):
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    count_vowels = 0
    count_consonants = 0
    for x in str(string):
        if x in vowels: 
            count_vowels +=1
        else:
            count_consonants +=1
            
    print('the number of vowels is:', count_vowels) 
    print('the number of consonants is:', count_consonants)


#5 define a function that accept n number and return n first number of fibonacci sequence
def fib_show(n): 
    n1,n2 = 0,1
    count = 0
    if n < 0: 
        print('please enter a positive number!')
    elif  n == n2: 
            print('the fibonanci sequences up to',n2,'is', n1)
    else:
        while count < n:
            nth = n1 + n2 
            n1 = n2
            n2 = nth
            count +=1

#6 define a function accept a radius function and return perimeter, area
def rad_cal(x): 
    if x < 0: 
        print('please enter a positive number!')
    else: 
        print('Perimeter =', x * 3.14 * 2)
        print('Area =', x**2 *3.14 )


#7 define a function accepts 2 arguments: 
#first: a list of integers
#second: a number with default value    
#repeat the list by the number then calculate average of all item in the list 

def func7(*list, x = 5):
    print(*list * x)


#________________________________________________________



