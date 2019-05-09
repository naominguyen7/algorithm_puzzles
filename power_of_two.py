"""Power of Two
Given an array AA. Is there any subset of array AA in which if we do AND of all elements of that subset then output should be in power of two (for example: 1, 2, 4, 8, 161,2,4,8,16 and so on).

Input
First line contains number of test cases TT. Each test first line contains NN size of array AA and next line contains NN space separated integers.

CONSTRAINTS:

1 \le T \le 10001≤T≤1000
1 \le N \le 2001≤N≤200
0 \le A_i \le 10^90≤A
​i
​​ ≤10
​9
​​
Output
For each test case print "YES" if there is any subset of array AA in which if we do AND of all elements of that subset then output should be in power of two else print "NO"."""


def stripped_inp():
    return input().strip()

def is_power_two(num):
    return (num and (num)&(num-1) == 0)

def contain_power():
    n = int(stripped_inp())
    arr = list(map(int, stripped_inp().split()))

    if n==1:
        return is_power_two(arr[0])

    total = 0
    max_bits = 32
    for i in range(max_bits):
        total |= (1<<i)

    for i in range(max_bits):
        ans = total
        for j in range(n):
            if arr[j] & (1 << i):
                ans &= arr[j]

        if is_power_two(ans):
            return True
    return False


if __name__=='__main__':
    t = int(stripped_inp())
    for _ in range(t):
        if contain_power():
            print("YES")
        else:
            print("NO")