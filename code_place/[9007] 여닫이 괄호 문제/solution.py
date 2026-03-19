def solution(num,bstr):
    ans = 0
    stack=[]
    answer=list()
    answer.append(0)
    for i in range(num):
        if bstr[i]=="(":
            stack.append(bstr[i])
        elif bstr[i]==')':
            if '(' in stack:
                ans +=2
                stack.pop(0)
            else:
                ans=0
        answer.append(ans)
    return max(answer)