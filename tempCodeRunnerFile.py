def sum_of_numbers(n):
    total = 0
    for i in range(n):
        number = int(input(f"Enter number {i+1}: "))
        total += number
    return total

n = int(input("How many numbers do you want to sum? "))
result = sum_of_numbers(n)
print(f"The sum of {n} numbers is: {result}")