with open('data.txt','w') as f:
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
print('No of vowels=',vowels,file=f)
print('No of consonants=',consonants,file=f)
print('No of spaces=',spaces,file=f)
f.close()
