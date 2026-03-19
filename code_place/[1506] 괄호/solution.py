n = int(input())
​
for i in range(n):
    arr=list(map(str, input()))
    stack=[]
    while arr !=[]:
        if arr[0] == '(':
            stack.append('(')
            arr.pop(0)
        else:
            if '(' in stack:
                arr.pop(0)
                stack.pop(0)
            else:
                break
    if arr == [] and stack == []:
        print('YES')
    else:
        print('NO')