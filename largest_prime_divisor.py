def generate_primes():
    l = 10000007
    marked = [True]*(l+2)
    marked[0] =marked[1] = False
    primes = []
    mid = int(l**0.5)
    for i in range(2, mid):
        if marked[i]:
            for j in range(i*2, l, i):
                marked[j] = False
            primes.append(i)
    for i in range(mid, l+2):
        if marked[i]:
            primes.append(i)
    return primes
PRIMES = generate_primes()

def largest_prime_divisor(n):
    n = abs(n)
    if n < 6:
        return -1
    res = -1
    num = 0
    for p in PRIMES:
        if p > n**.5:
            break
        if n%p:
            continue
        while n%p==0:
            n //=p
        res = p
        num +=1
    if num > 1:
        return max(res, n)
    if num and n > 1:
        return n
    return -1



if __name__ == "__main__":
    while True:
        n = int(input())
        if not n:
            break

        print(largest_prime_divisor(n))