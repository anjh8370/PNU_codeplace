import sys
​
arr = list(map(int, sys.stdin.readline().split()))
​
arr.remove(min(arr))
if arr==[]:
    print(-1)
else:
    aa = ' '.join(map(str, arr))
    print(aa)