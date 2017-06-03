#!/usr/bin/python

import random
import sys

for q in range(1000):
    line_raw = raw_input("What is your question?\n")
    # line_raw = 'meet+meet+meet+meet=team'
    print 'Got...', line_raw
    line = line_raw.replace(' ','')
    s = list(set(list(line.replace('+','').replace('=',''))))
    ll = line.split('=')
    xx = [list(x) for x in ll[0].split('+')]
    y  = list(ll[1])
    for k in range(100000):
        sd = {a:b for a,b in zip(s,random.sample(range(10), len(s)))}
        print 'trying...', sd
        if sd[y[0]] == 0:continue
        drop = False
        for x in xx:
            if sd[x[0]] == 0:
                drop=True
        if drop:continue
        int_y = int(''.join([str(sd[i]) for i in y]))
        int_xx = [int(''.join([str(sd[i]) for i in x])) for x in xx]
        if sum(int_xx) == int_y:
            print 'Answer:', int_y, int_xx
            break
