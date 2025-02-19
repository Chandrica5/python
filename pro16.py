s = input("Enter a str:")
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            print("first repeating ch:",s[i])
            exit()
print("no repeating ch")
