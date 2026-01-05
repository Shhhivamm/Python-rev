# aim: to find minimum number from the list.

#Create an empty list

lst = []
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    ele =int(input())
    lst.append(ele)
print(lst)
print("Largest number in the list is: ",max(lst))