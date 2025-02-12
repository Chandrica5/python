def find_missing_num(arr,n):
    expected_sum = n*(n+1)/2
    actual_sum = sum(arr)
    return expected_sum-actual_sum;
n = int(input("Enter value of n:"))
arr = list(map(int,input("Enter array of elements:").split()))
missing_num = find_missing_num(arr,n)
print("Missing num:",missing_num)
