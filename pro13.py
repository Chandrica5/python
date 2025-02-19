s = input("Enter  a string:")
vowels = "aeiouAEIOU"
vowel_count=0
consonant_count=0
for ch in s:
    if 'A'<= ch <= 'Z'or 'a' <= ch <= 'z':
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("vowel:",vowel_count)
print("consonant:",consonant_count)
