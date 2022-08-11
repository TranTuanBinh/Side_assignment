#1
def instr():
    print('Start message')
    input('Press Enter to continue')

    print('Step 1: Unplug the dryer and move it away from the wall.')
    input('Press Enter to continue')

    print('Step 2: Remove the six screws from the back of the dryer.')
    input('Press Enter to continue')
   
    print('Step 3: Remove the dryer’s back panel.')
    input('Press Enter to continue')
    
    print('Step 4: Pull the top of the dryer straight up.')
    input('Press Enter to continue')


#2
def rev_name(firstname, lastname):
    print(lastname, firstname)


#3
# This program calculates gross pay.
def main():
# Get the number of hours worked.
    try:
        hours = int(input('How many hours did you work?' ))
    except:
        print('insert integer')
        raise

# Get the hourly pay rate
    try:
        pay_rate = float(input('Enter your hourly pay rate:' ))
    except: 
        print('insert float')
        raise

# Calculate the gross pay
    gross_pay = hours * pay_rate

# Display the gross pay
    print(f'Gross pay: ${gross_pay:,.2f}')



