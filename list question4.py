''' Write a python program to input a list of integers and add a number
    entered by the user in every element
'''
lst1=eval(input())
lst2=[]
n=int(input())
for i in lst1:
  lst2.append(i+n)
print(lst2)
