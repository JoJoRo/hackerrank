#!/usr/bin/python3

def funny(list_n):
	ans = ('Not Funny', 'Funny')
	substractions = list(map(abs, [x-y for x,y in zip(list_n[0:-1], list_n[1:])]))
	boolean = (substractions == (substractions[::-1]))
	return ans[boolean]


T = int(input())
for _ in range(T):
	lis = list(map(ord, list(str(input()).strip())))
	print(funny(lis))
