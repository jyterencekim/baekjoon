from collections import defaultdict
import heapq

def input_and_split():
    return [int(x) for x in input().split()]

n, m = input_and_split()
nodes = defaultdict(set)
for _ in range(n - 1):
    x, y, d = input_and_split()
    nodes[x].add((y, d))
    nodes[y].add((x, d))

def solve(src, dst):
    visited = set()
    q = [(0, src)]
    while q:
        dist_sum, curr = heapq.heappop(q)
        visited.add(curr)
        if curr == dst:
            return dist_sum
        for adj, d in nodes[curr]:
            if adj not in visited:
                heapq.heappush(q, (dist_sum + d, adj))
    # cannot reach here
    return -1

ans = []
for _ in range(m):
    x, y = input_and_split()
    ans.append(solve(x, y))

for a in ans:
    print(a)