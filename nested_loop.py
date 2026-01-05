# rows= int(input("How many rows? : "))
# columns= int(input("How many columns? : "))
# symbols= input("Choose a symbol : ")


# Outer loop is responsible for computing the rows
# innner loop is responsible for computing the columns

# for row in range(rows):
#     for column in range(columns):
#         print(symbols, end="")
#     print()


for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end="")
    for k in range(1,i+1):
        print("*", end="")
    print()

for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ", end="")
    for k in range(1,i+1):
        print("*", end="")
    print()

for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end="")
    for k in range(1,i*2-1+1):
        print("*", end="")
    print()

 
for i in range(4,0,-1):
    for j in range(1,6-i):
        print(" ", end="")
    for k in range(1,(2*i-1)+1):
        print("*", end="")
    print()

    