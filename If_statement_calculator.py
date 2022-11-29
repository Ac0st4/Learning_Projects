# Building a calculator

num1 = float ( input ("Enter first number:  "))
op = input("Enter a operator [+, -, *, / ]:  ")
num2 = float ( input ("Enter the second number:  "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "/":
    print (num1 / num2)
elif op == "*":
    print (num1 * num2)
else:
    print("Invalid Operator")
w