a = int(input())
n=0
while a !=1 and n!=500:
  if a%2 == 0:
    a = a//2
  else:
    a=a*3+1
  n+=1
if n==500:
  print(-1)
else:
  print(n)