'''#ATM card 
correct_pin=1234
i=1
while i<=3:
    pin=int(input("enter your pin:"))   
    if pin==correct_pin:
        print("Access granted")
        break
    else:
        print("wrong pin")
    if i==3:
        print("card blocked")  
        break 
    i=i+1'''

#for i in range(10,0,-1):
#   print(i)
'''i=1
while i<=10:
    print(i)
    i=i+1'''
'''fruits=["apple","banana","papaya"]
for i in fruits:
    print(i[1])'''
'''n=int(input("enter a  number"))
for i in range(1,11):
    print(f"{n}x{i} = {n*i}")'''
'''for  i in range(1,11):
    if i==6:
        break
    print(i)'''

'''number=[1,4,7,9,45]
for i in range(len(number)):
    
        print(number[i])'''
'''i=1
while i<=10:
    if i%2==0:
      print(i)
    i=i+1'''
'''for  i in range(1,21):
      if i%3==0:
         continue
      print(i)'''
'''for i in range(1,4):
   for j in range(1,4):
       print(j, end="")
   print()'''
'''for i in range(1, 10):
    if i == 5:
        break
    print(i)
    print('Loop completed')'''
  # 1 multiplication table
'''n=int(input("enter a number:"))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")'''
#2 sum of numbers
'''n=int(input("enter a number:"))
sum=0
for i in range(n+1):
    sum=sum+i
print(sum)'''
#3.count even and odd numbers
'''n=int(input("enter n number:"))
even_count=0
odd_count=0
for i  in range(n+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even_count=",even_count)
print("odd_count=",odd_count)
'''
#prime number check
'''number=int(input("enter a number:"))
count=0
if number<=1:
    print("not a prime number")
for i in range(1,number+1):
    if number%i==0:
        count=count+1
if count==2:
   print("It is a prime number")
else:
  print("Not a prime number")'''
#palindrome check
'''number1=int(input("enter a number:"))
number2=number1
reverse=0
while number2!=0:
    digit=number2%10
    reverse=(reverse*10)+digit
    number2=number2//10
if number1==reverse:
   print(f"{number1} is a palindrome")
else:
    print(f"{number1} is not a palindrome")'''
#find factors
'''number=int(input("enter number:"))
for i in range(1,number+1):
    if number%i==0:
      print(i)'''
#Break challenge
'''for i in range(1,101):
    if i%7==0 and i%9==0:
       print(i)
       break'''
#continue challenge
'''for i in range(1,51):
    if i%3==0:
       continue
    print(i)'''
'''for i in range(1,6):
    for j in range(5-i):
        print("",end="")
    for k in range((2*i)-1):
            print("*",end="")
    print()'''
#pattern printing
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range((2 * i) - 1):
        print("*", end="")

    print()
# 10)number printing for second pattern
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()