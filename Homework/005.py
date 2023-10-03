'''
#Problem 1-------------
n = 1
n = (int(input("Value")))
sum = 0
for i in range(1, n+1):
    print(i)
    if (i%2==0):
        sum += i
print("--Sum--")
print(sum)
'''
#Problem 2-------------
'''
n = (int(input("Value")))

if n <=3:
    for i in range(n-2):
        for i in range(n):
            print("*   "*n)
'''
'''
for i in range(n-(n-1)):
        for i in range(n):
            print("*   "*n)

'''
#Problem 3-------------
''
n = (int(input("Value")))
factorial = 1
for i in range(1, n+1):
    print(i)
    factorial += i

print("--Factorial--")
print(factorial-1)
