s = input("Enter a string:")
new_str = " "
for ch in s:
    if ch not in new_str:
        new_str += ch
print("str without duplicates:",new_str)
