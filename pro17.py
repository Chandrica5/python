s=input("enter a str:")
converted=" "
for ch in s:
    if 'A'<=ch<='Z':
        converted += chr(ord(ch)+32)
    elif 'a'<=ch<='z':
        converted += chr(ord(ch)-32)
    else:
        converted += ch
print("converted:",converted)
        
