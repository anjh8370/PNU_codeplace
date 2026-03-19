k= int(input())
aa=[0,0] #인덱스 오류 방지용
w=[]#가로
h=[]#세로
bb=[0,0] #인덱스 오류 방지용
ans2=[] #리스트로 하는 이유는 경우에 따라 2가지가 추가될 수 있기 때문
for i in range(2,8):
    a,b=map(int, input().split())
    aa.append(a)
    bb.append(b)
    if a == 1 or a==2:
        h.append(b)
    else:
        w.append(b)
    if a == aa[i-2]: #입력 순서 상 이 둘이 첫번째로 같아야 빈 밭
        ans2.append(b*bb[i-1])
if ans2 == []:
    ans2.append(bb[2]*bb[7]) #입력순서가 314231일 경우
​
print((max(w)*max(h)-ans2[0])*k) #무조건 ans[0]이 빈 밭임 