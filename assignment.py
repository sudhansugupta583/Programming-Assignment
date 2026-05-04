# 1. Write a program to check whether the given number is in between 1 and 100 or not.
num=int(input("enter number="))
if num>=1 and num<=100:
    print("Number is between 1 and 100")
else:
    print("Number not b/w 1 and 100")
#2.Check whether the user input number is even or odd and  display it to user.
c_num=int(input("enter no.="))
if c_num%2==0:
    print(f"The given no. {c_num} is even.")
else:
    print(f"The given no.{c_num} is odd.")
# 3. Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, 
# where 1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. 
# The program should display an error message if the user enters a number that is outside the range of 1 to 12.
m=int(input("Enter a month number: "))
month={1:"January",2:"Feburary",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
if m in month:
    print("It is",month[m])
else:
    print("Number is entered is invalid")
# 4. A school has following rules for grading system:
#  a. Below 25 - F b. 25 to 45 - E c. 45 to 50 - D d. 50 to 60 - C e. 60 to 80 - B f. Above 80 - A Ask user to enter marks and print the corresponding grade.
marks=int(input("Enter your marks:"))
if marks>80:
    print("Your grade is A")
elif marks>=60 and marks<=80:
    print("Your grade is B")
elif marks>=50 and marks<60:
    print("Your grade is C")
elif marks>=45 and marks<50:
    print("Your grade is D")
elif marks>=25 and marks<45:
    print("Your grade is E")
else:
    print("Your grade is F")
#5. Write a program to check whether a number is divisible by 7 or not.
number=int(input("Enter number:"))
if number%7==0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")
#6. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
num1=int(input("Enter first No.:"))
num2=int(input("Enter second No."))
op=str(input("Enter Mathematical Operator:"))
if op=="+":
    print("Addision of given no. is:",num1+num2)
elif op=="-":
    print("Subtraction Of given no. is ",num1-num2)
elif op=="*":
    print("Multiplication of given no. is",num1*num2)
elif op=="/":
    print("Division of given no. is",num1/num2)
else:
    print("Invalid operator choosen")
#7. Write a Python program to check car loan eligibility: Salary >= 50,000 and Credit Score >= 700: "Eligible" Otherwise: "Not Eligible"
salary=int(input("Enter your salary:"))
credit=int(input("Enter your credit score:"))
if salary>=50000 and credit>=700:
    print("You're eligible for loan")
else:
    print("You're not eligible for loan")
# 8. Write a Python program that takes an integer input n n. From given number, check if it is divisible by both 3 and 5, and print "FizzBuzz" if true. 
# If the number is divisible only by 5, print "Buzz." If it is divisible only by 3, print "Fizz." Finally, if the number is not divisible by either 3 or 5, print the number itself.
n=int(input("Enter no.="))
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%5==0:
    print("Buzz")
elif n%3==0:
    print("Fizz")
else:
    print(n)
#9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.
ch=str(input("Enter Word="))
if "aeiou" in ch:
    print("It is vowel")
else:
    print("It is constant")
#10. Write a Python program to input marks and determine the grade based on the following conditions:90-100: A 
# 80-89: B 70-79: C Below 70: Fail
x=int(input("Enter your marks="))
if x>=90 and x<=100:
    print("A")
elif x>=80 and x<=89:
    print("B")
elif x>=70 and x<=79:
    print("C")
elif x<70:
    print("Fail")
else:
    print("Invalid marks")
#11. Write a Python program to categorize a person’s age: Age < 13: Child 13 <= Age <= 19: Teenager Age > 19: Adult
age=int(input("Enter Your Age:"))
if age<13:
    print("Child")
elif age>13 and age<=19:
    print("Teenager")
elif age> 19:
    print("Adult")
else:
    print("Invalid Input")
#12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.
char=input("Enter your character:")
if char.isupper():
    print(f"{char} is Uppercase ")
elif char.islower():
    print(f"{char} is Lowercase")
elif char.isdigit:
    print(F"{char} is a Digit")
else:
    print("Invalid or Special Charcater")
#13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").
print("1.Red\n2.Yellow\n3.Green")
col=int(input("enter your choice="))
if col==1:
    print("Stop")
elif col==2:
    print("Get Ready")
elif col==3:
    print("GO")
else:
    print("Invalid Input")
#14. Write a Python program to check eligibility for a job based on age and experience:
# Age > 18 and Experience >= 2 years: Eligible Otherwise: Not Eligible
agge=int(input("Enter Your Age:"))
exp=int(input("Enter Your Years Job Experience:"))
if age>18 and exp>=2:
    print("You're Eligible")
else:
    print("Not Eligible")
#15.. Write a Python program to give advice based on the temperature:Temperature > 30°C: "It's hot, stay hydrated!"
#Temperature between 15-30°C: "Enjoy the weather!" Temperature < 15°C: "It's cold, wear warm clothes!"
temp=int(input("Enter Temperature:"))
if temp>30:
    print("It's hot, stay hydrated!")
elif temp<30 and temp>15:
    print("Enjoy the weather!")
elif temp<15:
    print("It's cold, wear warm clothes!")
else:
    print("Invalid input")
#16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
# Pizza: $10 Burger: $7 Pasta: $8
menu=int(input("Enter Your Desired option 1.Pizza\n2.Burger\n3.Pasta"))
if menu==1:
    print("Pizza:$10")
elif menu==2:
    print("Burger:$7")
elif menu==3:
    print("Pasta:$8")
else:
    print("You have entered invalid input")
#17. Write a Python program to select players based on height: Height >= 6 feet: Selected Height < 6 feet: Not Selected
height=float(input("Enter Your height in ft"))
if height>=6:
    print("Selected")
elif height<6:
    print("Not Selected")
else:
    print("Invalid Input")
#18. Write a Python program to check if a person is eligible to watch a movie based on their age:
# Age >= 18: Allowed Age < 18: Not Allowed
ae=int(input("enter your age="))
if ae>=18:
    print("Allowed")
elif ae<18:
    print("NOT ALLOWED")
else:
    print("Invalid Input")
#19. Write a Python program to check login credentials:
# Username: "admin", Password: "password123" If correct, print "Access Granted"; otherwise, print "Access Denied."
usern=input("Enter Username=")
passs=input("Enter Your Password=")
if usern=="admin" and passs=="password123":
    print("Access Granted")
else:
    print("Access Denied")
#20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:
# 12, 1, 2: "Winter" 3, 4, 5: "Spring" 6, 7, 8: "Summer" 9, 10, 11: "Autumn"
mon=int(input("Enter month no.="))
if mon in (12,1,2):
    print("Winter")
elif mon in (3,4,5):
    print("Spring")
elif mon in(6,7,8):
    print("Summer")
elif mon in(9,10,11):
    print("Summer")
else:
    print("Invalid Input")