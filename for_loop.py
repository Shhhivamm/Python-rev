# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end = "")
#     print("")


# for i in range(1,7,1):
#     for j in range(0,i):
#         print("  *", end="")
#     print("")

# print("\n")
# for i in range(6,0,-1):
#     for j in range(0,i):
#         print("  *", end= "")
#     print("")
d=1
m=2
for i in range(6,0,-1):
    for j in range(0,i):
        print(" ", end="")
    for k in range(d):
        print("*", end="")
    for l in range(2,m):
        print("*", end="")
    d=d+1
    m=m+1
    print("")


r=6
for p in range(0,7,1):
    for u in range(0,p):
        print(" ", end="")
    for t in range(r):  
        print("*", end="")
    for z in range(r+1):
        print("*", end="")
       
    r=r-1
    print("")