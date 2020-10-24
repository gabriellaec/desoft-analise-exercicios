lista=[]
a=int(input('Digite um número diferente de 0:'))
while a!=0:
    lista.append (a)
    a=int(input('Digite um número diferente de 0:'))
if a==0:
    i=0
    s=0
    while i<len(lista):
        s+=lista[i]
        i+=1
print (s)