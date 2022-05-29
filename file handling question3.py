with open('data.txt','w') as f:
  d={}
n=int(input())
for i in range(n):
    k=eval(input())
    v=eval(input())
    d[k]=v
key=list(d.keys())
key.sort()
print(key,file=f)
f.close
