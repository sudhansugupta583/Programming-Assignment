#1
age=int(input("enter your age="))
height=int(input("enter height in cm="))
if age>=12 and height>=140:
    print("You're eligible")
else:
    print("Not eligible")
#2
li=int(input("Enter desired light\n1.Red\n2.Yellow\n3.Green\n="))
match li:
    case 1:
        print("Stop")
    case 2:
        print("Be Ready")
    case 3:
        print("Go")
    case _:
        print("Invalid Number")
#3
no=int(input("Enter number b/w 1 and 4: "))
match no:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _:
        print("invalid season number")
#4
user=input("Enter Username: ")
if user=="admin":
    password=input("Enter your password:")
    if password=="pass123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
#5
ag=int(input("Enter Your Age: "))
salary=int(input("Enter Your Salary: "))
credit=int(input("Enter Credit Score: "))
age_flag= ag>=21 and ag<=60
salary_flag= salary>=30000
credit_flag= credit>=700
if age_flag and salary_flag and credit_flag:
    print("Loan Approved")
elif not age_flag and not salary_flag and not credit_flag:
    print("Loan Denied as age doesnot fulfill criteria")
elif not age_flag:
    print("Loan Denied as Age is not b/w 21 to 60")
elif not salary_flag:
    print("Loan Denied due to Salary less than 30,000")
else:
    print("Loan Denied due to less credit score than 700")
#6
a=int(input("Enter Your Age: "))
member=input("Do You have membership card Y/N: ")
if a<12:
    print("No Ticket Fee Needed!!")
elif a>=12 and a<=60:
    if member=="Y" and member=="y":
        print("Ticket Cost:150")
    else:
        print("Ticket Cost:200")
elif a>60:
    print("You get a senior citizen discount\nYour ticket costs:100")
else:
    print("Invalid input")
#7
sal=int(input("Enter Salary: "))
ser=int(input("Enter Year's of Service: "))
if ser>5:
    bonus=ser*0.05
    print(f"Your bonus is {bonus}.")
else:
    print("You have service year less than 5 years so bonus=0")
#8
radius=float(input("Enter radius of citcle whose area is need to be calculated: "))
area=3.14*radius**2
print(f"Area of Circle is:{area}")
#9
gen=input("Enter Your Gender(M/F): ")
ge=int(input("Enter Your Age: "))
day=int(input("Enter Working Days: "))
if ge>=18 and ge<30:
    if gen=="M" and gen=="m":
        wm=700*day
        print(f"Your Wage is={wm}")
    elif gen=="F" and gen=="f":
        ww=750*day
        print(f"Your Wage is={ww}")
    else:
        print("Invalid Gender")
elif ge>=30 and ge<=40:
    if gen=="M" and gen=="m":
        wmm=800*day
        print(f"Your Wage is={wmm}")
    elif gen=="F" and gen=="f":
        www=850*day
        print(f"Your Wage is={www}")
    else:
        print("Ivalid gender")
else:
    print("Invalid Age ")
#10
num=int(input("Enter Number"))
if num%3==0 and num%5==0:
    print("Fizz Buzz")
elif num%3==0 and num%5!=0:
    print("Fizz")
elif num%3!=0 and num%5==0:
    print("Buzz")
elif num%3!=0 and num%5!=0:
    print(num)
else:
    print("Invalid Input")