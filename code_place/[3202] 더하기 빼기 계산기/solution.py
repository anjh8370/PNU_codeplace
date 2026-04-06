line = str(input())
answer=0
n = list(map(str, line.split('+')))
for i in n:
    if '-' in i:
        n1 = list(map(int, i.split('-')))
        answer += n1[0] - sum(n1[1:])
    else:
        answer+=int(i)
print(answer)