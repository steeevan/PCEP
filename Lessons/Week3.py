# If Elif Else

#Exercise 1

grade = "B"

if grade == "A":
  print("Good Job you got an A!")
elif grade == "B":
  print("Okay , You passed!")
elif grade == "C":
  print("You got  a C, Merp")
elif grade =="D":
  print("NO ")
else:
  print("You failed")
  
  # Exercise 2
  #Create a program that categorizes a person's age into categories like 
  #child, teenager, adult, or senior citizen using if, elif, and else.
  
age = 10
  
if 0 < age <= 12:
  print("Child")
  
  
numbers = [201,20,303,40,50,605,70,80,901,100]

for c in numbers:
  print(c)
  
for i in range(1,len(numbers),2):
  print(numbers[i])


for i in range(len(numbers)):
  if numbers[i] % 2 == 0:
    print(numbers[i], " is even")
  else:
    print(numbers[i], " is odd")
