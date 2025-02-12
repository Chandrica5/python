arr = list(map(int,input("Enter elements:").split()))
smallest = min(arr)
largest = max(arr)
for num in arr:
    if num < smallest:
        smallest=num
    if num > largest:
        largest=num
print("Largest:",largest)
print("Smallest:",smallest)
