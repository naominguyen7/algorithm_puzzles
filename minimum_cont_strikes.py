"""
Painting Fence
Bizon the Champion isn't just attentive, he also is very hardworking.

Bizon the Champion decided to paint his old fence his favorite color, orange. The fence is represented as nn vertical planks, put in a row. Adjacent planks have no gap between them. The planks are numbered from the left to the right starting from one, the i^{th}i
​th
​​  plank has the width of 11 meter and the height of a_ia
​i
​​  meters.

Bizon the Champion bought a brush in the shop, the brush's width is 11 meter. He can make vertical and horizontal strokes with the brush. During a stroke the brush's full surface must touch the fence at all the time (see the samples for the better understanding). What minimum number of strokes should Bizon the Champion do to fully paint the fence? Note that you are allowed to paint the same area of the fence multiple times.

Input
The first line contains integer nn (1 \le n \le 50001≤n≤5000) — the number of fence planks.

The second line contains nn space-separated integers a_1a
​1
​​ , a_2a
​2
​​ , ..., a_na
​n
​​  (11 \le≤ a_ia
​i
​​  \le≤ 10^910
​9
​​ ).

Output
Print a single integer — the minimum number of strokes needed to paint the whole fence.
"""
from sys import setrecursionlimit
def find_min_strokes(start, end, painted):
    if start >= end:
        return 0
    mini = start + arr[start: end].index(min(arr[start:end]))
    verticals = end - start
    recursive = arr[mini] - painted
    if recursive >= verticals:
        return verticals
    recursive += find_min_strokes(start, mini, arr[mini]) + find_min_strokes(mini+1, end, arr[mini])
    return min(recursive, verticals)

setrecursionlimit(10000)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_min_strokes(0, n, 0))