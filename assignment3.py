age=input("what is your age")
gender=input("what gender are you:male/female")
account_bal=0
#if (int(age)>25) and (age<30):
 # account_bal=account_bal + 100000
#else:
#print("sorry no money for you")

account_bal = input("enter your account_bal")
if(int(account_bal)>100000) and (int(account_bal)<200000):
    account_bal=account_bal - 25000
    print("we have deducted ksh 25000")
if(int(account_bal)>500000)and(int(account_bal)<1000000):
    account_bal = account_bal - (0.3*account_bal)
    print("we have deducted 30% from your account")
else:
    if(int(account_bal))>1000000:
        account_bal = account_bal - 15000
        print("we have deducted ksh 15000")        