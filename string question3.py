# Write a python program to find the frequency of characters
st=input("Enter the String ")
c=input("Enter the character to be searched ")
count=0
for i in st:
    if(i==c):
        count+=1
print(f'Frequency of {c} is {count}')
