def solution(A,B):
    n=0
    B=list(map(int, B.split()))
    for i in range(len(B)):
        if A == int(B[i]):
            n+=1
    return n
​