#
# """Topological Sorting
# Sandro is a well organised person. Every day he makes a list of things which need to be done and enumerates them from 11 to nn. However, some things need to be done before others. In this task you have to find out whether Sandro can solve all his duties and if so, print the correct order.
#
# Input
# In the first line you are given an integer nn and mm (1 \le n \le 100001≤n≤10000, 1 \le m \le 10000001≤m≤1000000). On the next mm lines there are two distinct integers xx and yy, (1 \le x, y \le 100001≤x,y≤10000) describing that job xx needs to be done before job yy.
#
# Output
# Print "Sandro fails." if Sandro cannot complete all his duties on the list. If there is a solution print the correct ordering, the jobs to be done separated by a whitespace. If there are multiple solutions print the one, whose first number is smallest, if there are still multiple solutions, print the one whose second number is smallest, and so on."""


from collections import defaultdict
from heapq import heappush, heappop


def BFS(v, e, result):
    indegree = [0] * (v+1)
    zero = []
    graph = defaultdict(list)

    for i in range(e):
        v1, v2 = map(int, input().strip().split())
        indegree[v2] += 1
        graph[v1].append(v2)

    for i in range(1, v+1):
        if indegree[i] == 0:
            heappush(zero, i)

    while len(zero):
        u = heappop(zero)
        result.append(u)

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(zero, v)

    for v in indegree:
        if v != 0:
            return False
    return True

if __name__ == "__main__":
    v, e = map(int, input().strip().split())
    result = []
    possible = BFS(v, e, result)

    if possible:
        print(" ".join(str(v) for v in result))
    else:
        print("Sandro fails.")