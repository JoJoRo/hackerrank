#!/usr/bin/env python3

# DETECT HTML links and print them

import re
import sys

pattern = '(?<=<a href=")(.*?)(?=/a>)'
com = re.compile(pattern)

T = int(input())
s = ''
for line in sys.stdin:
	s += line

m = com.findall(s)

pattern1 = '(.*?)(?=")'
com1 = re.compile(pattern1)

pattern2 = '(?<=">)(.*?)(?=<)'
com2 = re.compile(pattern2)

pattern3 = '(?<=<b>)(.*?)(?=</b>)'
com3 = re.compile(pattern3)

for i in m:
	aux1 = com1.findall(i)
	aux2 = com2.findall(i)
	if not aux2[0]:
		aux2 = com3.findall(i)
	s = aux1[0]+','
	if aux2:
		s += aux2[0].strip()
	print(s)
