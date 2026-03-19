A,B = map(int, input().split())
abc = [1,2,3]
if A not in abc:
  print('잘못된입력')
elif B not in abc:
  print('잘못된입력')
elif A-B ==0:
  print('무승부')
elif A-B ==1:
  print('A승B패')
elif A-B ==-2:
  print('A승B패')
elif A-B ==2:
  print('B승A패')
elif A-B ==-1:
  print('B승A패')