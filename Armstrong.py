def is_armstrong(num):
    digits = [int(digit) for digit in str(num)]
    num_of_digits = len(digits)
    sum_of_powers = sum([digit ** num_of_digits for digit in digits])
    return sum_of_powers == num
number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")