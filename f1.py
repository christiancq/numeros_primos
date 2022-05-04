def isPrime(n):
    n = abs(n)
    qtdDivisores = 0

    for i in range(1, n + 1):
        if n % i == 0:
            qtdDivisores += 1
    
    if qtdDivisores == 2:
        return True
    return False

for i in range(100001):
    isPrime(i)
