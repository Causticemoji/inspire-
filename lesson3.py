#print colours in uppercase using loop
from math import prod


sum_nums=0
prod_nums=1


#for number in range(0,20):
    # if(number %2==0):
     # sum_nums=sum_nums + number
#print(sum_nums)

for number in range(0,20):
     if(number %2==1):
       sum_nums=sum_nums+number
       # print(sum_nums)

for number in range(0,1000):
     if(number%2==1):
         prod_nums=prod_nums+6
#print(prod_nums)

for number in range(0,20):
    if (number%2==0):
       prod_nums =prod_nums+2
       print(prod_nums)
