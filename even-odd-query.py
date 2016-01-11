#!/usr/bin/env python3

def sol(x, y, l):
	aux = y - x
	if aux == 0:
		ans = l[x-1] % 2
	else:
		if aux == 1:
			if l[x] == 0:
				ans = 1
			else:
				ans = l[x-1] % 2
		else:
			if l[x] == 0:
				if l[x+1] == 0:
					ans == l[x-1] % 2
				else:
					ans = 1
			else:
				ans = l[x-1] % 2
	return ('Even', 'Odd')[ans]


int(input())
l = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
	x, y = list(map(int, input().split()))
	print(sol(x, y, l))
