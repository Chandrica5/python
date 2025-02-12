def right_rotate(arr,k):
    k %= len(arr)
    return arr[-k:]+arr[:-k];
arr = list(map(int,input("Enter elements:").split()))
k = int(input("Enter k:"))
result=right_rotate(arr,k)
print(result)
