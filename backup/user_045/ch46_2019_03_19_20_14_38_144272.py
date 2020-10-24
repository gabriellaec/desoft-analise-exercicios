l=[]
a=input('palavras?')
l.append(a)
i=0
while l[i]!='fim':
    if l[i][0]=='a':
        i+=1
    else:
        del l[i]
    a=input('palavras?')
    l.append(a)
print(l)        