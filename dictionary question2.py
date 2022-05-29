''' Write a python program to take the dictionary from the user 
    and print all it's keys in ascending order
'''
d={}
n=int(input())
for i in range(n):
    k=eval(input())
    v=eval(input())
    d[k]=v
key=list(d.keys())
key.sort()
print(key)
