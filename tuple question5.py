''' python progman to find product all the number in tuple'''

def multiple(num):
  temp = list(num)
  product = 1
  for i in temp:
    product*=i
  return product
num = (4,3,2,2)
print ("product is ",multiple(num))
