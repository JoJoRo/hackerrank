#!/usr/bin/env python3

import re

T = int(input())
l = list()
for i in range(T):
	l.append(input())

words = list()
for i in l:
	words.append(re.findall('\w+', i))

T = int(input())
for i in range(T):
	chain = input()
	print(sum([i.count(chain) for i in words]))
