with open('data.txt','w') as f:
  n=int(input('Enter the length of the list '))
lst=[]
for i in range(n):
    x=input()
    if(x!=' '):
        lst.append(x)
    else:
        break
print(lst,file=f)
f.close()
