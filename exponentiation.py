'''
Exponentiation


Exponentiation is the raising of one number to the power of another.
This operation is performed using two asterisks **.

Let's use exponentiation to solve a known problem.
You are offered a choice of either $1.000.000 or $0.01 (one penny)
doubled every day for 30 days (the resulting amount is doubled every day).

Task:
Write a program to calculate the amount that will result from the doubling
to understand which choice results in a larger amount.

'''

n = 0.01

days = 0

while days < 30:

    n = n * 2

    days += 1

if n > 1000000:
    print(f'The value of n is {n:,} and is greater than 1,000,000.\n')
    print(f'So, {n:,} is a better investment.')

else:
    print(f'The value of n is {n:,} and is less than 1,000,000.')
    print(f'So, {n:,} is not a better investment.')
