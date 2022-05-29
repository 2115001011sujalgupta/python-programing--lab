""" Write a python program to input a string by the user
    and print only the first character of each word
""" 
st=input()
l=len(st)
print(st[0],sep='.',end=' ')
for i in range(0,l):
    if(st[i]==' '):
        print(st[i+1],sep='.',end=' ')
