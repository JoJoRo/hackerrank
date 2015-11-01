#!/usr/bin/env python3

def deletions(lis):
	l = lis[0:-1]
	ans = [1 for i,x in enumerate(l) if x == lis[i+1]]
	return sum(ans)
		

T = int(input())
for _ in range(T):
	print(deletions(list(str(input()))))
	
