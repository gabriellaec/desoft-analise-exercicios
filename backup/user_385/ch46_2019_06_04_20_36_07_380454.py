l=[]
a=input('palavras?')
l.append(a)
i=0
while l[i]!='fim':
    if l[i][0]=='a':
        print(l[i])
        i+=1
    else:
        del l[i]
    a=input('palavras?')
    l.append(a)
  
       
       