s = input("Enter a string:")
for i in range(len(s)):
    unique = True
    for j in range(len(s)):
        if i!=j and s[i]==s[j]:
            unique=False
    if unique == True:
        print("First non repeating ch:",s[i])
        break
