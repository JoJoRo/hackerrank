#!/usr/bin/env python3

import re
import sys

patternEND = r"^[a-z\s]+ hackerrank$"
patternBEGIN = r"^hackerrank [a-z\s]+$"
patternONE = r"^hackerrank$"

regexpEND = re.compile(patternEND, re.IGNORECASE)
regexpBEGIN = re.compile(patternBEGIN, re.IGNORECASE)
regexpONE = re.compile(patternONE, re.IGNORECASE)
T = int(input())
for line in sys.stdin:
	resultEND = regexpEND.search(line)
	resultBEGIN = regexpBEGIN.search(line)
	resultONE = regexpONE.search(line)
	if resultEND:
		print(2)
	elif resultBEGIN:
		print(1)
	elif resultONE:
		print(0)
	else:
		print(-1)
		
