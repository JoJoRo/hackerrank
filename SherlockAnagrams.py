#!/bin/env python3

def sherlock(s):
	ans = 0
	d = dict()
	for i in range(len(s)):
		for j in range(i+1, len(s)+1):
			new = s[i:j]
			ordered = list(new)
			ordered.sort()
			ordered = ''.join(ordered)
			if ordered in d:
				d[ordered] += 1
			else:
				d[ordered] = 1
	for k in d:
		ans += (pow(d[k],2) - d[k])//2
	return ans


t = int(input())
for i in range(t):
	print(sherlock(input()))
