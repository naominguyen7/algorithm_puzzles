"""The number on the board
Some natural number was written on the board. Its sum of digits was not less than kk. But you were distracted a bit, and someone changed this number to nn, replacing some digits with others. It's known that the length of the number didn't change.

You have to find the minimum number of digits in which these two numbers can differ.

Input
The first line contains integer kk (1 \le k \le 10^91≤k≤10
​9
​​ ).

The second line contains integer nn (1 \le n < 10^{100000}1≤n<10
​100000
​​ ).

There are no leading zeros in nn. It's guaranteed that this situation is possible.

Output
Print the minimum number of digits in which the initial number and nn can differ."""

def min_changes(k, arr):
    res = 0
    dif = k - sum(arr[i]*i for i in range(1,10))
    i = 0
    while dif > 0:
        t = (dif-1)//(9-i)+1
        if arr[i] > t:
            res += t
            break
        res += arr[i]
        dif -= arr[i]*(9-i)
        i+=1
    return res



if __name__=="__main__":
    k = int(input())
    arr = [0]*10
    for i in input():
        arr[int(i)]+=1

    print(min_changes(k, arr))


