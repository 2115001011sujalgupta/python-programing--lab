dic = {'key1':'value1','key2':'value2','key3':'value3','key4':'value1','key5':'value3'}
sub = {}

for i in dic.values():
    if i not in sub:
        l=[]
        for k in dic:
            if dic[k]==i:
                l.append(k)
        sub [i]=l 
print ("new dictionary is :") 
print(sub)              
