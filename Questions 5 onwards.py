import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

for i in range(len(random_numbers)):


    if random_numbers[i] > 50:
        #random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)

    elif random_numbers[i] < 50:
        #Replace it with "XX"
        random_numbers[i] = "XX"

print(random_numbers)

# First I go through the list of 10 using index numbers, If number is greater than 50 I change it to one between 20 and 30 using random.randint
# if it is lower than 50, I use elif and make the number equal to XX, finally I print to see the output

print((3+10**2/2) or 70.0)

import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)