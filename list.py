# li = ['option 1', 'option 2', 'option 3']
# print(li)

# li.append("option 4")
# print(li)

# li.pop(0)
# print(li)

# print("\n","\n")
# total= 0
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l)
# for i in range(0,len(l)):
#     total= total+l[i]
# print("the sum of the numbers are : ",total)

# print("\n","\n")

# l2 = [5,3,7,1,9,2,4,8,6]
# for i in range(len(l2)):
#     for j in range(i + 1, len(l2)):
#         if l2[i] < l2[j]:
#             l2[i], l2[j] = l2[j], l2[i]  #swaping lists

# print(l2)

# ---------------------------    pushing all zeros in the end question    -----------------------------

# l3=[5,0,3,1,2,0,6,0,7,0]
# count = 0

# for i in range(len(l3)):
#     for j in range(i + 1, len(l3)):
#         if l3[i] > l3[j]:
#             l3[i], l3[j] = l3[j], l3[i]

# for k in range(len(l3)):
#     if l3[k] == 0:
#         count = count + 1
# # print(count)

# for d in range(count):
#     l3.pop(0)
#     l3.append(0)

# print(l3)

# ---------------------------    2d list m user se input wala question    -----------------------------

# lst = []
# for i in range(2):
#     lst2=[]
#     for j in range(1):
#         n = input("Enter your name : ")
#         a = int(input("Enter your age : "))
#         e= input("E-mail address : ")
#         c = int(input("Enter phone number : "))

#         lst2.append(n)
#         lst2.append(a)
#         lst2.append(e)
#         lst2.append(c)
#     lst.append(lst2)

# print(lst)

# ---------------------------    repeat/duplicate wala question    -----------------------------

# lis = [1, 1, 2, 1, 3, 4, 5, 1,5,4,3,2,5,2,5,6,7,8,4,2,5]
# uni=[]
# dup=[]

# for i in lis:
#     if i not in uni:
#         uni.append(i)
        
#     elif  i not in dup:
#         dup.append(i)

# print(uni)  
# print(dup) 

# ---------------------------    missing number wala question    -----------------------------

# li=[1,2,3,4,5,7,8,9]
# missings=[]
# for i in range(0,10):
#     if i not in li:
#         missings.append(i)
# print(missings)
# ---------------------------    total question       -----------------------------

# l=[1,2,3,4]

# print(len(l))

# count=0
# for i in range(len(l)):
#     count+=l[i]

# print(count)

# ---------------------------    Reverse sum wala question    -----------------------------

# a=input("enter the first position : ")
# one = a[0]
# three = a[1]
# first = three + one

# b = input("enter the second position : ")
# two = b[0]
# four = b[1]
# second = four + two

# a= int(a)
# b = int(b)
# total= a + b
# # print(total)

# first=int(first)
# second=int(second)
# totalreverse = first + second
# # print(totalreverse)

# totalreverse = str(totalreverse)
# x = totalreverse[0]
# y = totalreverse[1]

# totalreverse1 = y + x
# totalreverse1 = int(totalreverse1)
# # print(totalreverse1)

# if totalreverse1 == total:
#     print("reverse sum is same")

# else:
#     print("the numbers are not equal")

# ------------------------------- zeros end m push wala question ---------------------------------

# s= [0,1,0,2,0,3,0,4,0,5,0,6,0,7]

# for i in range(len(s)):
#     if s[i] == 0:
#         s.remove(0)
#         s.append(0)
        
# print(s)

#--------------------------------------------extend list------------------------------------------------

# l1=["pizza", "cholle bhature", "shake"]
# l2=["ice cream","cake","chocolate"]

# l1.extend(l2)

# print(l1)

# -------------------------------------------------------------------------------------------------------

# name = ['ajay','shivam', 'manish','sachin']
# name.sort()
# print(name)






