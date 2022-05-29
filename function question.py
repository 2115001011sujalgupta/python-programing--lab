''' Write a python program to creat a list whose elements are inputed by the user
    till the user enter a space
'''
n=int(input('Enter the length of the list '))
lst=[]
for i in range(n):
    x=input()
    if(x!=' '):
        lst.append(x)
    else:
        break
print(lst)
