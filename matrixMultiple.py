a = eval(input("Enter the first matrix: "))
b = eval(input("Enter the second matrix: "))
result =[[0 for _ in range(len(b[0]))] for _ in range(len(a))]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
            
print("Resultant matrix: ")
for row in result:
    print(row)