lista=[]
listanova=[]
numero=int(input('Digite números: '))
while numero>0:
    numero=int(input('Digite números: '))
    if  numero>0:
        lista.append(numero)
#len(lista)=len(listanova)
n=len(lista)
while 0<n:
    listanova.append(lista[n-1])
    n-=1
print(listanova)