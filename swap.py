def swap_without_temp(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    
    a = a + b  
    b = a - b  
    a = a - b  
    
    print(f"After swap: a = {a}, b = {b}")

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
swap_without_temp(a, b)
