def rev_arr(arr, k):
    n = len(arr)
    for i in range(0, n, k):
        arr[i:i+k] = reversed(arr[i:i+k])  
    return arr  

arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))
print("Reversed in groups:", rev_arr(arr, k))
