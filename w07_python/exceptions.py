import sys

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("Error: Must be a number")
    sys.exit(1)
    
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Can't divide by 0")
    sys.exit(1)
    

print(f"the result of {x}/{y} is {result}")
    

