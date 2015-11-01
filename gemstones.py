#!/usr/bin/env python3

R = int(input())

grid = []
for _ in range(R):
    grid.append(set(list(str(input()))))

a = set()
for i in grid:
    a = a.union(i)

ans = []
f = lambda x,y: x in y
for j in a:
    aux = [f(j,v) for v in grid if f(j,v) == True]
    if len(aux) == R:
        ans.append(j)

print(len(ans))
