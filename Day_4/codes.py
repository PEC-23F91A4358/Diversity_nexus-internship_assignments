#marks calculator

name=input("enter student_name:")
marks=int(input("enter  your marks:"))
if marks<0 or marks>100:
    print("invalid.please enter marks between 0 and 100")
elif marks <=100 and  marks >=90:
    print("Grade A excellent")
elif marks <90 and marks >= 75:
    print("Grade B very good")
elif marks <75 and marks >= 60:
    print("Grade C good ")
elif marks < 60 and marks >=50:
    print("Grade D you can improve")
else:
    print("Fail")

# job interview qualification

age=18
Qualification="B.tech"
skill="c#"
if age>=18 and Qualification == "B.tech" and (skill=="java" or skill=="python"):
    print("Eligible for interview")
elif age>=18 and Qualification == "B.tech" :
    print("conditionally eligible")
else:
    print("not eligible")

#name pass word verification

name="harshi"
login_password="1234"
user_name=input("enter user name:")
password=input("enter your password:")
if user_name ==name :
    if password ==login_password :
       admin=input( "Are you an admin ?")
       if admin=="yes":
          print("welcome admin.you have admin access")
       else:
          print("welcome user .you have noraml message.")
    else:
        print("wrong password")
else:
    print("wrong username.")

# bank application

account_status=input("is the account is active /inactive:")
account_balance=int(input("enter available money:"))
withdraw_money=int(input("how much you want:"))
daily_limit=int(input("maximum amount allowed to withdraw:"))
if account_status=="active":
    if withdraw_money>0:
        if withdraw_money<=daily_limit:
           if withdraw_money<=account_balance:
               print("withdrawal successful")
           else:
               print("insufficient balance")
        else:
            print("exceed daily limit")
    else:
        print("withdraw amount is invalid")
else:
    print("account is inactive")

#choices  

balance=5000
print("1.check balance")
print("2.money deposit")
print("3.money withdraw")
print("4.exit")
choice=int(input("enter your choice:"))
if choice==1:
    print("Balance:",balance)
elif choice==2:
    amount=int(input("how much money you want to deposit:"))
    balance+=amount
    print("New balance:",balance)
elif choice==3:
    withdraw=int(input("how much money want to withdraw:"))
    if withdraw<=balance:
        print("withdraw successful")
        balance-=withdraw
        print("new balance:",balance)
    else:
        print("Insufficient balance")
    balance-=withdraw
elif choice==4:
    print("Thank you")
else:
    print("Invalid choice")
