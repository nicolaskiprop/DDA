import sys
class Calculator:
    def add(self):
        x=int(input("Enter the first number: "))
        y=int(input("Enter the second number: "))
        result=x+y
        print("The sum is: ",result)
    def sub(self):
        x=int(input("Enter the first number: "))
        y=int(input("Enter the second number: "))
        result=x-y
        print("The difference is: ",result)
calc=Calculator()
operation=input("Enter the operation you want to perform: ")
if operation=="add":
    calc.add()
elif operation=="sub":
    calc.sub()
else:
    print("Invalid operation")
