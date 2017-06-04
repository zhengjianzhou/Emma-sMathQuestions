#!/usr/bin/python

import random,sys

while True:
    # line_raw = 'meet+meet+meet+meet=team'
    line = raw_input("What is your question?\n").replace(' ','')
    print 'Got : ', line
    s = set(line.replace('+','').replace('=',''))
    l_0, l_1 = line.split('=')
    xx, y = [x for x in l_0.split('+')], list(l_1)
    print xx,y
    while True:
        sd = {a:b for a,b in zip(s,random.sample(range(10), len(s)))}
        
        if sd[y[0]] == 0:continue
        drop = False
        for x in xx:
            if sd[x[0]] == 0:
                drop=True
        if drop:continue

        int_xx = [int(''.join([str(sd[i]) for i in x])) for x in xx]
        int_y = int(''.join([str(sd[i]) for i in y]))
        
        print 'trying...', sd, int_xx, int_y
        if sum(int_xx) == int_y:
            print 'Answer:', '+'.join([str(i) for i in int_xx]), '=', int_y
            break
