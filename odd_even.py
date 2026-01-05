def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

num = int(input("Enter a number: "))

check_odd_even(num)
