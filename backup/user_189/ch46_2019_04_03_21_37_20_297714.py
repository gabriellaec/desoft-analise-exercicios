a=[]
i=0
palavra=str(input('digite uma palavra: '))
while palavra!='fim':
    a.append(palavra)   
    palavra=str(input('digite uma palavra: '))         
while i<len(a):
    palavra=a[i]
    if palavra[0]=='a'and len(palavra)>1:
        print(palavra)
    i+=1