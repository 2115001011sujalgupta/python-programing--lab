''' Write a python program to creat a dictionary having key element 
    given by user's range and list as value which contains table of
    that number using dictionary comprension
'''

n=int(input())
m=int(input())
d={a:[a*for in range(1,11)] for a in range(n,m+1)}
print(d)
