#1.Write a program to remove the item present at index 4 and add it to the 2nd 
# position and at the end of the list. 
items=[3,5,7,9,11,13]
a=items.pop(4)
items.insert(2,a)
items.append(a)
print(items)
#2.Given two sets Write a code to identify their intersection. Remove these common elements specifically from the first_set.
first_set={23,42,65,57,78,83,29}
second_set={57,83,29,67,73,43,48}
common_set=first_set&second_set
if common_set:
    diff= first_set.difference(second_set)
    print(f"The new intersected set is {diff} and the common values were{common_set} ")
else:
    print("Nothing common!!")
#3.Write a program to determine if first_set is a subset or superset of second_set. If a relationship is found,
#  delete all elements from the set that is identified as the subset.
f={27,43,34}
s={34,93,22,27,43,53,48}
if f.issubset(s) or f.issuperset(s):
    f.clear()
    print("First set is the subset or superset of second set ")
else:
    print("First set isn't the subset or superset of second set ")
#4.Given a dictionary month containing names and numerical values, write a script to extract all values and 
# store them in a list. Ensure the final list contains no duplicate values.
month={'jan':47,'feb':52,'mar':47,'apr':44,'may':52,'jun':53,'jul':54,'aug':44,'sep':54}
neww=list(set(month.values()))
print(neww)
#5.Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number
sample=[87,41,45,65,94,41,91,99,94]
tup=tuple(set(sample))
print("The maxium value is:",max(tup),"\nThe minimum value is:",min(tup))
#6.Write a Python program that defines two sets: The program should check whether the two clubs have any members in common.
#  If they do, print the following members exist in both groups and if they have no common members, print no overlapping members found between groups
club_A={'Ram','Shyam','Hari'}
club_B={'Ram','Gita','Hari'}
com=club_A&club_B
if com:
    print(f"The following members {com} exist in both groups")
else:
    print("No Overlapping members found in groups")
#7.Define required_tasks and completed_tasks.Write a program to verify if all required tasks have been finished by checking if
# required_tasks is a subset of completed_tasks. Print all tasks done or some tasks pending accordingly
required_task={"Email",'Report','Meeting'}
completed_task={"Email",'Report'}
if required_task.issubset(completed_task):
    print("All Required task has been completed")
else:
    print("Some Task pending accordingly")
#8. Create a dictionary mapping student names to email addresses. Write a program that prompts the 
# user for a name. If the name exists, display the email, otherwise display contact not found.
di={'ram':"ram@email.com",'hari':'hari@email.com','shyam':'shyam@email.com','raju':'raju@email.com'}
name=input("Enter Name whose email you wanna get: ")
print(di.get(name, "Contact Not Found"))
#9.Define shopping_list and bought as sets. Compute the set difference to identify unbought items. If items remain, print them
# if the difference is empty, print Shopping complete
shopping={'Milk','Bread','Eggs'}
bought={'Bread','Eggs'}
fin=shopping.difference(bought)
if fin!=set():
    print(f'{fin} remains!!!!')
else:
    print("Shopping Complete")
#10.Starting with write a program to add a new_student.The student should only be added if they are not already in the list. Print a
# confirmation or an already present message.
class_list=['ram','sita','laxman']
new_student=input("Enter Student To Add: ").lower()
if new_student in class_list:
    print("Already Present!!!!!")
elif class_list.append(new_student):
    print("Added Succesfully!")
else:
    print("Invalid Input!!!!")
#11.Given a list of votes, Write a script to count the occurrences of Blue. If the count is 3 or higher, print
# Blue wins; otherwise, print Blue did not win.
vote=['Blue','Red','Blue','Green','Blue',]
co=vote.count('Blue')
if co>=3:
    print("Blue wins")
else:
    print("Blue didn't win")
#12.Using a dictionary of student grades write a program to check if a specific student's name exists as a key.
# If found, print their grade; otherwise, indicate that the grade is not available.
grades={'ram':92,'sita':88}
na=input("Enter Name whose grade to be printed: ")
print(grades.get(na,"Grades Not Available"))
#13.A company accepts an application only if: The candidate knows Python or Java, and has at least 2 years of experience. Check
# if at least one skill in applicant[‘skills’] is in required_skills, and experience >= 2. Print priya qualifies or priya does not qualify
applicant={'name':'priya','skill':['java','sql'],'expericence':1}
required_skill={'java','python'}
skill=list(required_skill)
reo=applicant['skill']
if skill[0] in required_skill or skill[1] in required_skill:
    if applicant['expericence']>=2:
        print('Priya Qualifys')
    else:
        print("Priya Doesn't Qualify")
else:
    print("Priya Doesn't Qualify")
#14.Write a Python program that determines whether an airline passenger’s cabin
# baggage is allowed based on two rules: The baggage weight must be 7 kg or less.
# The item being carried must not be in banned_items.
# Prompt the user to enter the baggage weight and the name of the item. Convert
# the item input to lowercase to ensure case-insensitive comparison. If both
# conditions are satisfied weight <= 7 and item not banned, print Bag allowed.
# Otherwise, print Bag not allowed
banned={'scissor','knife','lighter'}
weight=int(input("Enter weight of baggage: "))
ban=list(banned)
it=input("Enter items (scissor or knife or lighter) if you have in in your baggage: ").lower()
if it not in ban and weight<=7:
    print("Bag Allowed")
else:
    print("Bag Not Allowed")
#15.Write a program to change shyam salary to 8500 in the following dictionary.Given:
sample_dict={'emp1':{'name':'John','salary':'7500'},
             'emp2':{'name':'Emma','salary':'8000'},
             'emp3':{'name':'Shyam','salary':'500'}}
sample_dict['emp3']['salary']=8500
print(sample_dict)
#16.Store two sets of items for Ram and Laxman. Determine if they have zero items in
#common. Print they picked completely different items or they have some common items based on the result.
ram={'milk','tea','cocacola','sprite'}
laxman={'milk','mountain dew','tea','pepsi'}
if ram.isdisjoint(laxman):
    print("They picked completely different items")
else:
    print("They have some common items")


