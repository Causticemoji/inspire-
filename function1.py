#!/usr/bin/python
#functions in python
#functions;block of codewhich gets 
#initializing function
#calling a function

from cmath import sqrt


def say_hello():
    print("hello from jkuat");x=4;y=7;z=x+y
say_hello()

def bark():
    print("dogs bark woof woof")
bark()

def moows():
    print("cows moows")
moows()

def roars():
    print("lion roars")
roars()

def purr():
    print("cats purr")
purr()

def neighs():
    print("horse neighs")
neighs()

def add_numbers(x,y):
    sum_numbers=x+y
    print("the sum of x+y is",sum_numbers)    
add_numbers(40,50)
add_numbers(100,440)
add_numbers(1,4)

def multiply_numbers(x,y):
    product_numbers=x*y
    print("the product of x*y is",product_numbers)
multiply_numbers(40,50)
multiply_numbers(100,440)
multiply_numbers(1,4)
#################
import math
a=int(input("coefficient of first term(a)"))
b=int(input("coefficient of second term(b)"))
c=int(input("enter the constant"))
def find_roots(a,b,c):
    y1=(-b+math.sqrt((b**2)-4*a*c))/(2*a)
    y2=(-b-math.sqrt((b**2)-4*a*c))/(2*a)
    print("the roots of the quadratic equation are:",y1,y2)
find_roots(a,b,c)
     