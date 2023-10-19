#Vocabulary
'''
abs() is a function used to find the absolute value of a rational number

a parameter is a place to insert the value to be manipulatied and to be placed in a temperary
variable's place

an argument is a way of storing information whether it is a list or a variable.

return statement is what the function lets out after running the variables through.

a conditional statements are things like if and elif, it is a condition to pass through.

a list is a way of storing many types of information at once. You can change what
is in it and easily extract things from it using the slicing. - (List[x])

a string are words between ".  ex:   "hello"

a loop is a way of repeating a function untill the requirments are met or for a specific
ammount of times.

a variable is a way of storing information that can only hold one thing at once. it can also hold any
type of data.

a dictionary is a list but with keys that can be accessed and changed.

'''

#programing probs

'''AVRAGE'''
num = [2,3,5]
def avrg(List):
    pls = 0
    for i in (range(len(List))):
        pls += List[i-1]
    pls = pls / len(List)
    return (pls)
print(avrg(num))

'''palindrome'''
def Pali(Check):
    FP = Check[::-1]
    if FP == Check:
        return True
    else:
        return False
print(Pali("Lorem Ipsum muspI meroL"))
print(Pali("Lorem Ipsum"))
'''string reversal'''
def strRV(RV):
    return RV[::-1]
print(strRV("Lorem Ipsum"))











