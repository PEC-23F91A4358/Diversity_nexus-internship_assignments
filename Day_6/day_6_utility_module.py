#Task1
#celsius to fahrenhiet:
def celsius_fahrenheit(temp):
    fahrenheit=(temp*9/5)+32
    return fahrenheit
result=celsius_fahrenheit(44)
print(result)
#fahrenheit to celsius:
def fahrenheit_celsius(temp):
    celsius=(temp-32)*5/9
    return celsius
result=fahrenheit_celsius(53)
print(result)
#TASK2

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
res=is_even(14)
print(res)
  
#TASK 3

def is_prime(number):
    count=0
    for i in range(1,number+1):
        if number%i==0:
           count+=1
    if count==2:
        return True
    else:
        return False
result=is_prime(77)
print(result)

#TASK 4

def is_palindrome(value):
    number2=value
    reverse=0   
    while number2!=0:
        digit=number2%10
        reverse=(reverse*10)+digit
        number2=number2//10
    if  value==reverse:
        print(f"{value} is a palindrome")
    else:
        print(f"{value} is not a palindrome")
is_palindrome(1221)

#TASK 5

def grade(marks):
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
grade(95)


#TASK 6:

def calculate_total(price, quantity):
    return price * quantity

print(calculate_total(200, 4))


#Task7

def add_all(*numbers):
    total=0
    for num in numbers:
        total=total+num
    
    print(total)
add_all(13,5,6,12)


#TASK 8

def build_profile(**details):
    print("Name:",details["name"])
    print("course:",details["course"])
    print("age:",details["age"])
    print(details)
build_profile(name="harshi",age=21,course="ai")

#TASK 9

def greet(name="sukrutha",city="Hyderabad"):
    print(f"Hello,myname is {name} and i lived in{city} ")
greet()
greet("Harshitha")
greet("harshi","Nellore")

#TASK 10

def average(*number):
    avg=0
    for i in number:
        avg=avg+i
    avg=avg/len(number)
    return avg
result=average(10,20,30,40)
print(result)
#minimum
def minimum(*number):
    min=number[0]
    for i in number:
        if min>i:
            min=i
    print(min)
minimum(1,45,89,1,56,56,0)
#maximum

def maximum(*number):
    max=number[0]
    for i in number:
        if max<i:
            max=i
    print(max)
maximum(1,45,89,1,56,56,0)
