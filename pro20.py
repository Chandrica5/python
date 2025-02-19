arr=list(map(int,input("enter arr:").split()))
even =[]
odd= []
for num in arr:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
arr = even+odd
print("result:",arr)
