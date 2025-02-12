arr = list(map(int,input("Enter elements:").split()))
x = int(input("Enter element to check the count:"))
count =0
for num in arr:
    if num==x:
        count +=1
print("occurence:",count)
