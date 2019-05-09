"""Permutation pp is an ordered set of integers p_1p
​1
​​ ,  p_2p
​2
​​ , ..., p_np
​n
​​ , consisting of nn distinct positive integers, each of them doesn't exceed nn. We'll denote the i^{th}i
​th
​​  element of permutation pp as p_ip
​i
​​ . We'll call number nn the size or the length of permutation p_1p
​1
​​ ,  p_2p
​2
​​ , ..., p_np
​n
​​ .

You have a sequence of integers a_1a
​1
​​ ,  a_2a
​2
​​ , ..., a_na
​n
​​ . In one move, you are allowed to decrease or increase any number by one. Count the minimum number of moves, needed to build a permutation from this sequence.

Input
The first line contains integer nn (1 \le n \le 3 * 10^5)(1≤n≤3∗10
​5
​​ ) — the size of the sought permutation. The second line contains nn integers a_1a
​1
​​ ,  a_2a
​2
​​ , ..., a_na
​n
​​  (-10^9 \le a_i \le 10^9)(−10
​9
​​ ≤a
​i
​​ ≤10
​9
​​ ).

Output
Print a single number — the minimum number of moves."""

def min_moves(n):
    arr = list(map(int, input().split()))
    stores = [0]*(n+1)
    outsides = []
    moves = 0

    for i in range(n):
        if 0 < arr[i] < n+1 and not stores[arr[i]]:
            stores[arr[i]] = 1
        else:
            outsides.append(arr[i])
    outsides = sorted(outsides, reverse=True)
    for i in range(1, n+1):
        if not stores[i]:
            moves += abs(outsides.pop() - i)
    return moves

if __name__ == '__main__':
    n = int(input())
    print(min_moves(n))