a=str(input('palavra:'))
while a!='fim':
    lista=[]
    if a[0]=='a':
        lista.append(a)
    a=str(input('palavra:'))
i=0
while i<len(lista):
    print(lista[i])
    i+=1
