''' Write a python program to enter a list of string from the user 
    and display the sorted list according to length
'''
lst=eval(input())
out=lst.sort(key=len)
print(out)
