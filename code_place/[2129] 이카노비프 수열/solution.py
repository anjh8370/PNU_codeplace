n = int(input())
arr = [1,1]
for i in range(n-2):
    arr.insert(0,sum(arr[0:2]))
print(' '.join(str(s) for s in arr[0:n]))