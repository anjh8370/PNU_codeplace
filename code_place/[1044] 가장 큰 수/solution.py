number = list(map(str, input().split()))
number.sort(key = lambda x: x*3, reverse = True)
if number[0] !='0':
    print(''.join(number) )
else:
    print('0')