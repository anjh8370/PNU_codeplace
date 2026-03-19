import sys
n=int(input())
​
for i in range (n):
    score=list(map(int, sys.stdin.readline(). split()))
        
        
    nn=score[0]
    avr=(sum(score[1:]))/nn
    std = 0
    for k in range (nn+1):
        if score[k-1] > avr:
            std +=1
    percent = 100*std/nn
    print('%.3f%%' % percent)