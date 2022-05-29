''' Write a python program to enter a user input list of integers and print only 
    the even numbers in a new list
'''
lst1=eval(input())
lst2=[]
s=0
for i in lst1:
  if(i%2==0):
    lst2.append(i)
print(lst2)
