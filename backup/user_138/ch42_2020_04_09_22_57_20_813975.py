lista=[]
palavra=input('palavra?')
i=0
while palavra!='fim':
    lista.append(palavra)
    palavra=input('outra palavra')
    
while i<len(lista):
    a=lista[i]
    if a[0]=='a':
        print (a)
    i+=1