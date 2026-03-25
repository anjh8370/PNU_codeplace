S=input()
stack = ''
cnt = 0
for i in S:
    if stack != i:
        cnt+=1
        stack = i
​
print(cnt//2)