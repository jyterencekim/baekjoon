import sys
sys.setrecursionlimit(10**6)

N = int(input())
g = []
for _ in range(N):
	g.append(input())

def get_adjacents(r: int, c: int):
	if r > 0:
		yield r - 1, c
	if c > 0:
		yield r, c - 1
	if r < N - 1:
		yield r + 1, c
	if c < N - 1:
		yield r, c + 1

def count(mergeables: set[chr]) -> int:
	seen = set()
	result = 0

	def probe(src: chr, r: int, c: int):
		if (r, c) in seen:
			return

		seen.add((r, c))
		for nr, nc in get_adjacents(r, c):
			if (nr, nc) in seen:
				continue
			if g[nr][nc] == src or (src in mergeables and g[nr][nc] in mergeables):
				probe(src, nr, nc)

	for r in range(N):
		for c in range(N):
			if (r, c) not in seen:
				result += 1
				probe(g[r][c], r, c)

	return result

a = count({})
b = count({'R', 'G'})

print(a, b)