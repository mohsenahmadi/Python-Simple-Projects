# This Program is a simple calculator. it's can be add, subtract, multiply and divide between two numbers.
#Also, I handled division by zero;)

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

if choice == '1':
	print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
	print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
	print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
	if num2 == 0:
		print("THIS ACTION IS NOT VALID")
	else: 
		print(num1,"/",num2,"=", divide(num1,num2))
else:
	print("Invalid input")
