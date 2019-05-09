"""Roma and Changing Signs
Roma works in a company that sells TVs. Now he has to prepare a report for the last year.

Roma has got a list of the company's incomes. The list is a sequence that consists of nn integers. The total income of the company is the sum of all integers in sequence. Roma decided to perform exactly kk changes of signs of several numbers in the sequence. He can also change the sign of a number one, two or more times.

The operation of changing a number's sign is the operation of multiplying this number by -1−1.

Help Roma perform the changes so as to make the total income of the company (the sum of numbers in the resulting sequence) maximum. Note that Roma should perform exactly kk changes.

Input
The first line contains two integers nn and kk (1 \le n, k \le 10^51≤n,k≤10
​5
​​ ), showing, how many numbers are in the sequence and how many swaps are to be made.

The second line contains a non-decreasing sequence, consisting of nn integers a_ia
​i
​​  (|{a_i}| \le 10^4)(∣a
​i
​​ ∣≤10
​4
​​ )."""

def max_income():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = sum(arr)
    contain_zero = False
    if arr[0] > 0:
        if k % 2 ==0:
            return res
        else:
            return res - 2*arr[0]
    for i in range(n):
        if not k:
            return res
        if not arr[i]:
            contain_zero = True
            break
        elif arr[i] > 0:
            break
        res -= 2 * arr[i]
        k -= 1

    if k % 2 == 0:
        return res
    elif contain_zero:
        return res

    if arr[i] < 0:
        return res + 2 * arr[i]
    elif -arr[i - 1] > arr[i]:
        return res - 2 * arr[i]
    else:
        return res + 2 * arr[i - 1]


if __name__=='__main__':
    print(max_income())

