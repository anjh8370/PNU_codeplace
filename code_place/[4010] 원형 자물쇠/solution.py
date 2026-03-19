a, b = map(str, input().split())
b= '1'+b
key = list(map(int, b))
answer=0
for i in range(len(b)-1):
  A = abs(key[i]-key[i+1])
  B = int(a) - A
  answer+=min(A,B)
print(answer)