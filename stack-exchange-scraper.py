#!/usr/bin/env python3

import re
import sys

pattern1 = '<div class="summary">[\s]*<h3><a href="/questions/(\d+)/[\w|-]+?" class="question-hyperlink">(.+)</a></h3>'
pattern2 = '<span title=".+" class="relativetime">(.+)?</span>'
com1 = re.compile(pattern1)
com2 = re.compile(pattern2)

s = ''
for line in sys.stdin:
	s += line

m1 = com1.findall(s)
m2 = com2.findall(s)

for n,i in enumerate(m1):
	aux = list()
	aux.append(i[0])
	aux.append(i[1])
	aux.append(m2[n])
	s = ';'.join(aux)
	print(s)
