#!/usr/bin/env python3

# Identifying comments on ide
# Use http://pythex.org/
import sys
import re

pattern = '(/\*(?:.|\n)*?\*/)|(//.*)'
comment = re.compile(pattern)

s = ''
for line in sys.stdin:
	s += line

words = comment.findall(s)

for i in words:
	for j in i:
		if j:
			# remove spaces after \n
			aux = j.split('\n')
			aux = [k.strip() for k in aux if k]
			for q in aux:
				print(q)
