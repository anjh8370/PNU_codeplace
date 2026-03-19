w, h =map(int,input().split())
ans=0
for i in range(w):
    n=h/w*i
    ans+=int(n)
print(ans*2)