i=2
c=2
Tam_lista=0
a=c
while c<=1000:
    lista=[]
    i=c
    lista.append(i)
    while i!=1:
        if i%2==0:
            i=i/2
            lista.append(i)
        else:
            i=(3*i)+1
            lista.append(i)
    if Tam_lista<len(lista):
        Tam_lista=len(lista)
        a=c
    c+=1
print(a)