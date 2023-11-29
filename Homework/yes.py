1: C
2: D
3: D
4: D
5: B
6: B
7: A
8: C
9: D
10: A

def calculate_area(radius):
  pi = 3.14159
  area = pi*radius**2
  return area

x = calculate_area(10)
print(x)


list = [1,2,3,4,5]
def sum_even_numbers(tlist):
  total = 0
  for i in range(len(tlist)):
    if tlist[i]%2 == 0:
      total += tlist[i]
  return total

y = sum_even_numbers(list)
print(y)
  

def safe_divide(a,b): 
  try:
    quotient = a/b
    return quotient
  except ZeroDivisionError:
        return "Error"

z = safe_divide(10,0)
print(z)
