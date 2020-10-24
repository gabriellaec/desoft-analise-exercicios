p=[]
a=input('digite uma palavra: ')
while a!='fim':
    p.append (a)
    a=input('digite uma palavra: ')
i=0
while i<len(p):
    if p[i][0]=='a':
        print (p[i])
    i=i+1