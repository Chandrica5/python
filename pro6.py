arr = list(map(int, input("Enter elements:").split()))
unique_arr = list(dict.fromkeys(arr))
print("After removal of duplicates:",unique_arr)
