def print_array(A, n):
    for i in range(n):
        print(A[i], end=" ")
    print()

def merge(A, mid, low, high):
    i = low
    j = mid + 1
    k = low
    B = [0] * 100

    while i <= mid and j <= high:
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
            k += 1
        else:
            B[k] = A[j]
            j += 1
            k += 1

    while i <= mid:
        B[k] = A[i]
        k += 1
        i += 1

    while j <= high:
        B[k] = A[j]
        k += 1
        j += 1

    for i in range(low, high + 1):
        A[i] = B[i]

def merge_sort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(A, low, mid)
        merge_sort(A, mid + 1, high)
        merge(A, mid, low, high)

if _name_ == "_main_":
    A = [9, 1, 4, 14, 4, 15, 6]
    n = len(A)
    print_array(A, n)
    merge_sort(A, 0, n - 1)
    print_array(A, n)