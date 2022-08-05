#1------------------
high_score = 95
#Get the first test score
first_test_score = int(input('insert your first test score: '))

#Get the second test score 
second_test_score = int(input('insert your second test score: '))

#Get the third test score 
third_test_score = int(input('insert you third test score: '))

#Get the average score
avg_test_score = (first_test_score + second_test_score + third_test_score) / 3
print(avg_test_score)
#Conditional statement
if avg_test_score > high_score: 
    print('Congratulation')
else: 
    print('Goodluck next test')


#2------------------
# Get the number of worked hours
worked_hours = int(input('insert your worked hours:'))

#Get the hourly pay rate
pay_rate = int(input('insert your pay rate'))

otm = 1.5 #overtime multiply
base_hours = 40 
ott = worked_hours - base_hours


if worked_hours > base_hours: 
    otp = ott * otm * pay_rate
    gross_pay = base_hours * pay_rate + otp 
    print(f'your gross pay is {gross_pay}')

else: 
    n_gross_pay = worked_hours * pay_rate
    print(f'your gross pay is {n_gross_pay}')



#3---------------------
salary = int(input('insert your salary: ')) #insert salary 
years_on_job = float(input('insert your years on job:')) #insert years on job 

min_salary = 30000
min_years_on_job = 2 

if salary >= min_salary: 
    if years_on_job >= 2: 
        print('you are qualified for the loan')
    else: 
        print('you must have been on your current job for at least 2 years to qualify')
     
else: 
    print('you must earn at least 30000 per year to be qualify ')


#4-------------------
for x in range(5): 
    print('hello world')

#5-------------------


while keep_going == 'y':
     sales = int(input('insert the sales:   '))
     comm_rate = float(input('insert the commisstion rate:  '))
     commission = comm_rate * sales 
     print(commission)
     keep_going = input('press y to calculate another commission')




