''' Write a function in python to check whether a number is palindrome or not'''
def palindrome(x):
  num=x
  rev=0
  while(x!=0):
    d=x%10
    x=x/10
    rev=rev*10+d
  return rev==num

n=int(input())
out=palindrome(n)
if out:
  print('Palindrome')
else:
  print('Not Palindrome')
