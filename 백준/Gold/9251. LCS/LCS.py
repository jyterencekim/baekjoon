def solve(x: str, y: str):
    X, Y = len(x), len(y)
    if X < Y:
        return solve(y, x)
    if Y == 0:
        return 0
    
    lcs = [[0 for _ in range(X + 1)] for _ in range(Y + 1)]
    
    for r in range(1, Y + 1):
        for c in range(1, X + 1):
            if x[c - 1] == y[r - 1]:
                lcs[r][c] = lcs[r - 1][c - 1] + 1
            else:    
                lcs[r][c] = max(lcs[r - 1][c], lcs[r][c - 1])
    
    return lcs[-1][-1]
    

a = input()
b = input()

result = solve(a, b)

print(result)