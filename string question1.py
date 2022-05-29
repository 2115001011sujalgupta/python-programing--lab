# Write a python program to count the number of vowles and consonants in a user entered string
st=input()
vowels=0
consonants=0
spaces=0
for i in st:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
        vowels=vowels+1
    elif(i==' '):
        spaces+=1
    else:
        consonants+=1
print('No of vowels=',vowels)
print('No of consonants=',consonants)
print('No of spaces=',spaces)
