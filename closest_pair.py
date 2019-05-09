"""The Closest Pair Problem
Given a set of points in a two dimensional space, you will have to find the distance between the closest two points.

Input
The input contains several testcases.

Each testcase starts with an integer NN (0 \le N \le 100000≤N≤10000), which denotes the number of points in this test.

The next NN line contains the coordinates of NN two-dimensional points. The first of the two numbers denotes the XX-coordinate and the latter denotes the YY-coordinate.

The input is terminated by a test in which N = 0N=0. This test should not be processed.

The value of the coordinates will be less than 4000040000 and non-negative.

Output
For each test produce a single line of output containing a floating point number (with four digits after the decimal point) denoting the distance between the closest two points. If there is no such two points whose distance is less than 1000010000, print the line INFINITY."""
from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def exhaustive_find(arr):
    res = float('inf')
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            t = distance(arr[i], arr[j])
            if res > t:
                res = t
    return res


def find_strip(px, py, d, best_pair):
    len_arr = len(px)
    midx = px[len_arr//2][0]

    sy = [p for p in py if midx - d <= x[0] <= midx + d]

    best = d

    for i in range(len(sy) - 1):
        for j in range(i+1, min(i+7, len(sy))):
            p1, p2 = sy[i], sy[j]
            dist = distance(p1, p2)
            if dist < best:
                best_pair = p, q
                best = dist
    return best_pair[0], best_pair[1], best

def find_closest(xarr, yarr):
    len_arr = len(xarr)
    if len_arr < 4:
        return exhaustive_find(xarr)

    mid = len_arr//2
    Lx = xarr[:mid]
    Rx = xarr[mid:]

    midx = xarr[mid][0]
    Ly = []
    Ry = []

    for x in yarr:
        if x[0] <= midx:
            Ly.append(x)
        else:
            Ry.append(x)

    p1, q1, mi1 = find_closest(Lx, Ly)
    p2, q2, mi2 = find_closest(Rx, Ry)

    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    p3, q3, mi3 = find_strip(xarr, yarr, d, mn)

    if d <= mi3:
        return  mn[0], mn[1], d
    else:
        return p3, q3, mi3


if __name__ == "__main__":
    while 1:
        n = int(input())
        if not n:
            break

        arr = []
        for i in range(n):
            arr.append(list(map(int, input().split())))
        xarr = sorted(arr)
        yarr = sorted(arr, key=lambda x: x[1])
        p1, p2, mi = find_closest(xarr, yarr)