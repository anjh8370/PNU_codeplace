pair = {')': '(', ']': '['}
​
while True:
    balanced = True
    line = str(input())
    stack=[]
    if line == '.':
        break
    for i in line:
        if i in '[(':
            stack.append(i)
        elif i in')]' and stack :
            if stack[-1] == pair[i]:
                stack.pop(-1)
            else:
                balanced = False
                break
        elif i in'])'and not stack:
            balanced = False
            break
    if balanced and not stack:
        print('yes')
    else:
        print('no')