''' 1
    12
    123
    1234
    12345
'''
r=int(input())
for i in range(1,r+1):
  for j in range(i):
    print(j+1,end='')
  print()
