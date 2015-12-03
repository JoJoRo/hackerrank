#!/usr/bin/env python2

import re
import sys

pattern = '(http[s]?)://(www)?\.?([\w|\.|-]+)(?=[/|\s|"|?])'
com = re.compile(pattern)

s = ''
T = int(input())
for line in sys.stdin:
    s += line
ans = com.findall(s)
l = list()
for i in ans:
    l.append(i[2])
l = list(set(l))
l.sort()
l = [i for i in l if '.' in i]
print(';'.join(l))
