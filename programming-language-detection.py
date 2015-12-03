#!/usr/bin/env python3

import re
import sys

patternC = '#include|#define|<[\w]+.h>|printf|for\([^\)]+\)|int main|scanf|->|assert'
patternPython = 'import |print |\'\'\'|def '
patternJava = 'public|static|void|main|System.out.print|import java[\.\w\*]+;'
comJava = re.compile(patternJava)
comPython = re.compile(patternPython)
comC = re.compile(patternC)
dJava = dict()
dPython = dict()
dC = dict()
for line in sys.stdin:
    ansC = comC.findall(line)
    ansPython = comPython.findall(line)
    ansJava = comJava.findall(line)
    for i in ansC:
        if i in dC:
            dC[i] += 1
        else:
            dC[i] = 0
    for i in ansPython:
        if i in dPython:
            dPython[i] += 1
        else:
            dPython[i] = 0
    for i in ansJava:
        if i in dJava:
            dJava[i] += 1
        else:
            dJava[i] = 0
ansC = sum([dC[i] for i in dC])
ansPython = sum([dPython[i] for i in dPython])
ansJava = sum([dJava[i] for i in dJava])
ans = [ansC, ansPython, ansJava]
print(('C', 'Python', 'Java')[ans.index(max(ans))])
