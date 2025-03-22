def is_prime(n):
    if (n<2):
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def next_prime(n):
    if not is_prime(n):
        return "it is not a prime number"
    nextnum=n+1
    while not is_prime(nextnum):
        nextnum+=1
    return nextnum
num=int(input(""))
print("next prime:",next_prime(num))
