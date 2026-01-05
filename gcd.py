a = int(input("Enter 1st number: "))

b = int(input("Enter 2nd number: "))

# def gcd(a, b):
#     if(b == 0):
#         return a
    
#     else: 
#         return gcd(b, a%b)
    
# print("The gcd of two numbers is: ",gcd(a,b))
gcd = 1
for i in range(1,min(a,b)+1):
    if a%i ==0 and b%i==0:
        gcd = i
print(f"gcd of {a} and {b} is: ",gcd)