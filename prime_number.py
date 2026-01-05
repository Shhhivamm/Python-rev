# a= int(input("enter your number:-"))

# if a%1 == 0 and a%3 != 0 and a%5 != 0 and a%7 != 0 and a%a == 0 or a == 2:
#     print("Numebr is prime.")
# elif a%2 == 0:
#     print("Numeber is composite.")

# else:
#     print("Number is composite")

a = int(input('Enter your number:-'))
b = 0
for i in range(2,a):    
    if a % i == 0:
        b += 1
if b == 0:
    print("prime")
else:
    print(a,"is non prime")
    