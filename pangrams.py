#!/usr/bin/python3

ans = ('not pangram', 'pangram')
s = str(input()).lower()
st = set(list(s))
al = set(list('abcdefghijklmnopqrstuvxyz'))
print(ans[al.issubset(st)])
