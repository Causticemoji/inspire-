#write a program to check if number is divisible by 7
number=int(input("enter a number"))
if(number%5==0)and(number%7==0):
 print(f"thenumber{number}is divisible by both 5 or 7")
else:
    print(f"thenumber{number}is not divisible by 5 or 7")