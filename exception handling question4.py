print('start')
lst=[1,2,3,4,5]
try:
  out=lst[2]
  print(out)
except:
  print('Invalid Index')
finally:
  print('stop')
