''' write a python program to take a dictionary from the user and remove a element 
    entered by the user
'''
d={}
n=int(input())
value=eval(input())
for i in range(n):
    k=eval(input())
    v=eval(input())
    d[k]=v
for i in range(n):
    if(d[i]==value):
        del d[i]
    else:
        print('Invalid key')
print(d)
