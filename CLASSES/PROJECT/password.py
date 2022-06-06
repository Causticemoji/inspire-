from lib2to3.pgen2.pgen import generate_grammar
import random
from sqlite3 import IntegrityError
import string
print('welcome to our password generator')
character='emmanuel254!'
#ask user number of passwords they want to generate
#convert the num_password into integer
#ask user for password length
#convert password to Integer
#print("hear are your passwords")
num_pass=int(input("write your preffered numbers"))
sym_pass='deno123'
len_pass=int(input("how many characters would you like"))
for password in range (num_pass):
    password=''
    for c in range  (len_pass):
        password+=random.choice(sym_pass)
    print(password)