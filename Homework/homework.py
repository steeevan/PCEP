1: A function are lines of code that only run when called upon, and it can bundle up instructions for a program and can be reused neatly

2: Parameters are the temporary variables in the function, and they are the placeholders for the actual values of the function.

3: An argument is a value passed to a function when used.

4: The return statement sends back the results of the function to the caller.

5: Programming constructs that allow programs to flow under certain conditions and specifications.

6: A data structure that is mutable, it can contain things like strings, integers, floats, etc.

7: A set of words; “Hello”

8: A loop repeats something over and over again until a certain condition is met.

9: A variable is used to hold a value, it can be temporary and used to hold value for certain conditions.

10: A dictionary is used to store data values within its key:value pairs.


listy = [1,2,3,4,5]

def average(tlist):
  total = 0
  for i in range(len(tlist)):
    total += tlist[i]
  average = total/len(tlist)
  return average

x = int(average(listy))
print(x)


num1 = 8
num2 = 476

def maximum(a,b):
  if a > b:
    return a,"is bigger"
  if b > a:
    return b,"is bigger"
  if a == b:
    return "idk"
  else:
    return "ERROR"
 
numbers = maximum(num1,num2)
print(numbers)

string = "racecar"

def palindrome(stringy):
  i = len(stringy)
  if stringy[0:i] == stringy[::-1]:
    return True
  return False

coolio = palindrome(string)
print(coolio)

biggylist = [2,5,6,8]
def Reversal(tlisty):
  return tlisty[::-1]
  
listerine = Reversal(biggylist)
print(listerine)


dict = {"Age":13,"Name":"Jasper","Birthday":"April 19","Height":"6 feet"}

def dicty(dictionary,key):
  return dictionary[key]
  
d = dicty(dict,"Name")
print(d)
