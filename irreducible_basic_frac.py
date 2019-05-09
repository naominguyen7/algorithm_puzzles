def num_ibf(n):
    if n == 1:
        return 1
    i = 2
    res = n
    while i <= n**.5:
        if n%i:
            i+=1
            continue
        while n%i == 0:
            n //= i
        res = res//i*(i-1)
        i += 1


    if n > 1:
        res = res // n * (n - 1)

    return res




if __name__ == "__main__":
    while True:
        n = int(input())
        if not n:
            break

        print(num_ibf(n))