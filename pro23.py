def highest_factor(digit):
    if digit==0|digit==1:
        return digit
    for i in range(digit//2,0,-1):
        if digit%i==0:
            return i
    return digit
def replace_with_highest_factor(num):
    place=1
    result=0
    while num>0:
        digit=num%10
        num//=10
        highest=highest_factor(digit)
        result=(highest*place)+result
        place*=10
    return result
num=int(input(""))
print("ans:",replace_with_highest_factor(num))
    
