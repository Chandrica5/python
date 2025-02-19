arr = list(map(int, input("Enter numbers: ").split()))
n = len(arr)
count = 0 

for i in range(n):
    if arr[i] != 0:
        arr[count], arr[i] = arr[i], arr[count]  
        count += 1

print("Modified array:", *arr)
