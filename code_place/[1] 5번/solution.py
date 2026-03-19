def solution(l1,l2):
    a, b = 0, 0
    for i in range(0,len(l1)):
        a+=l1[i]*10**i
    for i in range(0,len(l2)):
        b+=l2[i]*10**i
    c = a+b
    line=list(map(int, str(c)))
    line.reverse()
    return line