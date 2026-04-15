t = int(input())
p = [0,1,1,1,2,2]
for k in range(95):
    p.append(p[-1]+p[-5])
for i in range(t):
    n = int(input())
    print(p[n])