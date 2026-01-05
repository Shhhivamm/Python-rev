def binarySearch(num, item):
    low = 0
    high = len(num) - 1

    while low <= high:
        mid = (high + low) // 2

        if item == num[mid]:
            return mid
        elif item > num[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

num = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    num.append(ele)

num.sort()
print("Sorted list:", num)

item = int(input("Enter the element to find: "))

result = binarySearch(num, item)

if result == -1:
    print("Element not found...")
else:
    print("Element is found at index", result)
