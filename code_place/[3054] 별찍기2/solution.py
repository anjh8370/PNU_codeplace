n=int(input())
for i in range(n):
  a=''
  for k in range(n):
    if k < n-i-1:
      a+=' '
    else:
      a+='*' 
  print(a)