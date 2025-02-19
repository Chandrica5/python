arr=list(map(int,input("enter arr:").split()))
pos =[]
neg= []
for num in arr:
    if num>0:
        pos.append(num)
    else:
        neg.append(num)
arr = neg+pos
print("result:",arr)
