def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


print("Click the Appropriate Number for Operations: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

n = int(input("Enter the Number of Operation you want to perform: "))

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

if n==1:
    print(add(a, b))

elif n==2:
    print(sub(a, b))

elif n==3:
    print(mult(a, b))

elif n==4:
    print(div(a, b))

else:
    print("Please run the code again, and give the appropriate input.")

