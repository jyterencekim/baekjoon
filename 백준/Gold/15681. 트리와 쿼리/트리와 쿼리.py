import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

def input_and_split():
    return map(int, sys.stdin.readline().split())

n, root, q = input_and_split()
graph = defaultdict(set)

for _ in range(n - 1):
    x, y = input_and_split()
    graph[x].add(y)
    graph[y].add(x)

counts_rooted_at = dict()

def count_nodes(r, parent=-1):
    if r in counts_rooted_at:
        # cannot happen
        return counts_rooted_at[r]
    
    count = 1 # including itself
    for adj in graph[r]:
        if adj != parent:
            count += count_nodes(adj, r)
    counts_rooted_at[r] = count
    return count

count_nodes(root)

for _ in range(q):
    i = int(sys.stdin.readline())
    print(counts_rooted_at[i])

