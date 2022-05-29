with open('data.txt','r') as f:
  a=int(input())
  b=int(input())
  out=a+b
  print(out,file=f)
  f.close()
