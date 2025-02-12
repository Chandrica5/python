arr = list(map(int,input("Enter the elements:").split()))
if (all (arr[i] <= arr[i+1] for i in range(len(arr)-1))):
    print("array is sorted")
else:
    print("array is not sorted")
