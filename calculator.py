num1 = float(input("Enter 1st number: "))
operator = input("Choose an Operator (+ , - , * , / ): ")
num2 = float(input("Enter 2nd number: ")) 

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")

print("The result is: ", result)