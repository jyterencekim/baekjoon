from collections import defaultdict

def input_and_split():
	return [int(x) for x in input().split()]

n, m = input_and_split()
rels = defaultdict(set)
leaves = {x for x in range(n)}
for _ in range(m):
	x, y = input_and_split()
	rels[x].add(y)
	rels[y].add(x)

def solve():
	def dfs(x, visited):
		if len(visited) == 5:
			return True
		for friend in rels[x]:
			if friend not in visited:
				visited.add(friend)
				found = dfs(friend, visited)
				visited.remove(friend)
				if found:
					return True
		return False

	for person in range(n):
		found = dfs(person, {person})
		if found:
			print(1)
			return

	print(0)

solve()