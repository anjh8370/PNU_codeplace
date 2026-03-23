idx = 1
while True:
  L, P, V = map(int,input().split())
  if L+P+V == 0:
    break
  days = (V//P)*L+min(L, V%P)
​
  print(f'Case {idx}: {days}')
  idx+=1