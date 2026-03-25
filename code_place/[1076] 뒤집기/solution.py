S=input()
stack = ''
cnt = 0
for i in S:
    if stack != i:
        cnt+=1
        stack = i
​
print(int(cnt/2))