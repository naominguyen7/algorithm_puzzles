"""Anagrammatic Primes
A number greater than one is prime if it has no divisors other than itself and 11 (note that 11 is not prime). For example, 2323 is prime and 3535 is not prime because 35 = 7 * 535=7∗5. When the digits of a number are rearranged, its primeness may change — for example, 3535 is not prime but 5353 is. For this problem, you have to find numbers which are prime no matter how you rearrange their digits. For example, all of the numbers 113, 131113,131 and 311311 are prime, so we say that 113113 is an anagrammatic prime (also 131131 and 311311 are anagrammatic primes).

Input
Each line of input will contain a single positive number nn, less than 1000000010000000. You must find the first anagrammatic prime which is larger than nn and less than the next power of 1010 greater than nn. The input will be terminated by a line consisting of a single 0.

Output
For each number in the input, one line of output must be produced. This output line should contain either the next anagrammatic prime, as described above, or 0 if there is no anagrammatic prime in the range defined."""
from itertools import permutations, combinations_with_replacement

def gen_primes():
    l = 10000000
    marked = [True]*l
    mid = int(l**.5+1)
    marked[0] = marked[1] = False
    for i in range(2, mid):
        if not marked[i]:
            continue
        for j in range(2*i, l, i):
            marked[j] = False
    res = [False]*l
    for i in range(2,8):
        for num in combinations_with_replacement('1379',i):
            ps = [int(''.join(e)) for e in permutations(num)]
            for p in ps:
                if not marked[p]:
                    break
            if marked[p]:
                for p in ps:
                    res[p] = True
    res[2] = res[3] = res[5] = res[7] = True
    return res



PRIMES = gen_primes()

def anagrammic(n):
    for i in range(n+1, n*10):
        if PRIMES[i]:
            return i
    return 0

if __name__=="__main__":
    for i in range(10000000):
        if PRIMES[i]:
            m = i
    n = int(input())
    while n:
        if n >=m:
            print(0)
        else:
            print(anagrammic(n))
        n = int(input())