def isPrime(n):
    n = abs(n)
    
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    
    stop = int(n ** 0.5) + 1
    
    for i in range(3, stop, 2):
        if n % i == 0:
            return False
    
    return True

for i in range(100001):
    isPrime(i)
