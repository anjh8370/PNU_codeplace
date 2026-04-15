number = list(map(str, input().split()))
number.sort(key = lambda x: x*3, reverse = True)
print(''.join(number) if number[0] !='0' else '0' )