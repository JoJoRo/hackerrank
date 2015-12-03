#!/usr/bin/env python2
import sys
import re

pattern = '([\w|\.]+@[\w|\.]+[a-z]{2,3})'
com = re.compile(pattern)
s = set()
input()
for line in sys.stdin:
    ans = com.findall(line)
    for i in ans:
        s.add(i)
s = list(s)
s.sort()
print ';'.join(s)
