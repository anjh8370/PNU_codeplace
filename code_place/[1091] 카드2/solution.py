n=list(range(1,int(input())+1))
​
while len(n)!=1:
    n.pop(0)
    n.append(n[0])
    n.pop(0)
print(n[0])