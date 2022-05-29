with open('data.txt','w') as f:
  def prime(a):
  s=0
  for i in range(1,a+1):
    if(a%1==0):
      s+=1
  return s==2
n=int(input())
out=prime(n)
if(out==True):
  print('Prime',file=f)
else:
  print('Not Prime',file=f)
  f.close()
