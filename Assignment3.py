#4. Design a program for a 'Student Resource Portal.' The program should ask for a username and a password.
#  If the username is admin and password is ad123, printAccess Granted: Faculty Dashboard
#  If the username is student and password is st2026, print Access Granted: Notes and Practice Questions
#  For any other combination, print Invalid Credentials.Please try again.
user=input("Enter Username= ")
p=input("Enter Password= ")
if user=="admin" and p=="ad123":
    print("Access Granted: Faculty Dashboard")
elif user=="student" and p=="st2026":
    print(" Access Granted: Notes and Practice Questions")
else:
    print("Invalid Credentials.Please try again.")
#5.Write a Python program that calculates a customer's final bill basedon their spending and membership status. 
# The program should follow the exact logic shown in the flowchart.
u=int(input("enter your purchase amount= "))
if u>5000:
    i= input("Do you have mebership y/n: ").lower()
    if i=="y":
        ud=0.2*u
        ud2=u-ud
        print(f"Final Amout={ud2}\nYou saved={ud}")
    else:
        print(f"Final Amount{u}")
else:
    print(f"Final Amount{u}")
#6.Create a Python program for a text-based adventure game called Magic Forest based on the given flowchart. 
# The program should follow the exact logic shown in the flowchart.
t="Welcome To The Magic Forest"
print(t.center(100))
s1=input("Enter Direction (North Or South): ").lower()
if s1=="north":
    print("Game Over!!!!")
else:
    s2=input("Do You Wanna Cross the river(r) or Follow the path(p): ").lower()
    if s2=="p":
        print ("Cross the River\n THE END")
    else:
        s3=input("Choose Fairy,Ogre, or Elf: ").lower()
        if s3=="elf":
            print("Congrats!!!!\nYou Win")
        else:
            print("Game Over!!!\nThe End!")
#10.Write a Python program that calculates a person’s Body MassIndex and determines their weight category based on the following rules:
# Ask the user to input their weight in float. Ask the user to input their height in float.
# Calculate the BMI using the formula: BMI = weight / height² Determine the weight status according to this criteria:
# Underweight if BMI < 18.5 Normal weight if 18.5 <= BMI <= 25 Overweight if 25 <= BMI <= 30 Obese if BMI >=30 
# Finally, print the result in the following format:Weight: 70 Height: 1.75 BMI: 22.9 Normal weight
w=int(input("Enter Your weight: "))
h=float(input("Enter Your Height(in meters): "))
h1=h*0.305
b=w/(h1**2)
if b<18.5:
    print(f"Weight:{w}\nheight:{h}\nBMI:{b} Underweight")
elif b>=18 and b<25:
    print(f"Weight:{w}\nheight:{h}\nBMI:{b} Normal")
elif b>=25 and b<30:
    print(f"Weight:{w}\nheight:{h}\nBMI:{b} Over weight")
elif b>=30:
    print(f"Weight:{w}\nheight:{h}\nBMI:{b} Obese")
else:
    print("Invalid Input")
#12.A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. 
#   Ask user for their salary and yea of service and print the net bonus amount.
emp=int(input("Enter Your Salary:"))
y=int(input("Enter Years Of Service:"))
if y>5:
    bo=0.05*emp
    print(f"Your Net Bonus is:{bo}")
else:
    print("NO bonus service year less than 5 years.")
#16.A utility company charges different rates based on electricity usage:
# If usage < 100 units then cost Rs 5 per unit If usage is between 100 to 300 units: First 100 units: Rs 5
# Next units: Rs 8 If usage is > 300 units: First 100: Rs 5 Next 200: Rs 8 Remaining: Rs10
use=int(input("Enter Units of Electricity Used: "))
if use<=100:
    c_1=use*5
    print(f"The Cost of {use}unit of electricity is Rs{c_1}")
elif use>100 and use<=300:
    c_2=((use-100)*8)+500
    print(f"The Cost of {use}unit of electricity is Rs{c_2}")
elif use>300:
    c_3=((use-300)*10)+2100
    print(f"The Cost of {use}unit of electricity is Rs{c_3}")
else:
    print("Invalid Input")
#18. Write a Python program that takes a number as input, first checks if it is positive if yes then 
# check whether it is even or odd.
no=int(input("Enter Your Number: "))
if no>0:
    if no%2==0:
        print("Positive Even No.")
    else:
        print("Positive Odd No.")
else:
    print("Negative No.")
#20. Create a weight conversion program that:Asks the user what their Earth weight is as a float. Asks
# the user for a planet number as an int.Then, use an if/elif/else statement to calculate the user's weight on
# the destination planet. To calculate the user's weight: destination weight=Earth weight×relative gravity
weight=float(input("Enter Your Earth Weight: "))
planet=int(input("Enter Planet no. from 1-7: "))
match planet:
    case 1:
        print("Weight on mercury is:",weight*0.38)
    case 2:
        print("Weight on venus is:",weight*0.91)
    case 3:
        print("Weight on mars is:",weight*0.38)
    case 4:
        print("Weight on jupiter is:",weight*2.53)
    case 5:
        print("Weight on saturn is:",weight*1.07)
    case 6:
        print("Weight on uranus is:",weight*0.89)
    case 7:
        print("Weight on neptune is:",weight*1.14)
    case _:
        print("Invalid Planet No.")
#21. WAP which accepts marks of four subjects and display totalmarks, percentage and grade. Hint: more than 70 –> distinction, more
# than 60 –> first, more than 40 –> pass, less than 40 –> fail
e=float(input("Enter Marks for english: "))
m=float(input("Enter Marks for maths: "))
s=float(input("Enter Marks for science: "))
c=float(input("Enter Marks for computer: "))
to=e+m+s+c
per=to/4
if per>70:
    print(f"Totalmarks:{to}\nPercentage:{per}\nGrade:Distinction")
elif per>60:
    print(f"Totalmarks:{to}\nPercentage:{per}\nGrade:First")
elif per>40:
    print(f"Totalmarks:{to}\nPercentage:{per}\nGrade:Pass")
elif per<40:
    print(f"Totalmarks:{to}\nPercentage:{per}\nGrade:Fail")
else:
    print("Invalid Input")
#21. Write a program that simulates the elevator's internal logic. Theprogram should accept user inputs for the desired floor, the current weight
# load, and the door status, then determine if the elevator is cleared to move.
# Requirements
# Target Floor: An integer representing the user's selection.Total Weight: A numerical value (in kg) representing the current load inside
# the lift.Door Status: A Boolean or string indicating whether the door is closed or open.Logic Constraints Floor Validation
#  The elevator only services floors in the range of 0 to 10.  If the input is outside this range, the system must display INVALID FLOOR and terminate the process.
# Weight Limit Sensor  The safety limit for this lift is 500kg.  If the total weight is greater than 500kg, the system must
# display OVERWEIGHT: LIFT CANNOT MOVE and terminate.Door Mechanism Status  The lift cannot move unless the door is fully engaged/closed.
#  If the door is open, display WARNING: CLOSE THE DOOR and terminate If all three conditions are met, the program should output: ACTIVATE
# ELEVATOR MOTION.
flo=int(input("Enter Desired Floor: "))
load=float(input("Enter Current Weight Load in the Lift: "))
door=int(input("Enter Door Staus\n1.Closed\n2.Open or Not fully closed\n: "))
if flo>=0 and flo<=10:
    if load<=500:
        if door==1:
            print("Activate Elevator Motion")
        else:
            print("Warning!! Close The Door!")
    else:
        print("Overweight!!! Lift Cannot Move")
else:
    print("Invalid Floor No.")