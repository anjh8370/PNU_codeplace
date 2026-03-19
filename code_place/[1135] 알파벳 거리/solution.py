n = int(input())
​
for i in range(n):
    ans=[]
    a, b = map(str, input().split())
    print('Distances:', end=' ')
    for k in range(len(a)):
        D = ord(b[k])-ord(a[k])
        if D < 0:
          D+=26
        ans.append(str(D))
​
    print(' '.join(ans))
        