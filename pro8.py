arr = list(map(int,input("Enter elements:").split()))
min_val=0
max_diff=arr[0]
for num in arr[1:]:
    max_diff = max(max_diff, num-min_val)
    min_val = min(min_val,num)
print(max_diff)
