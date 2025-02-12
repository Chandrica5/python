def max_sum_rotation(arr):
    n = len(arr)
    total_sum = sum(arr)
    curr_val = sum(i * arr[i] for i in range(n))

    max_val = curr_val
    for i in range(1, n):
        curr_val = curr_val + total_sum - n * arr[n - i]
        max_val = max(max_val, curr_val)
    
    return max_val

arr = list(map(int,input("Enter elements:").split()))
print(max_sum_rotation(arr))  
