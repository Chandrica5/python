arr = list(map(int, input("Enter numbers (0s,1s,2s): ").split()))
count0 = count1 = count2 = 0

for num in arr:
    if num == 0:
        count0 += 1
    elif num == 1:
        count1 += 1
    else:
        count2 += 1

arr = [0] * count0 + [1] * count1 + [2] * count2
print("Sorted array:", *arr)
