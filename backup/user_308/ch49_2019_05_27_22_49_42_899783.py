lista=[]
x=int(input('Digite o número desejado: '))
while x>0:
    lista.append(x)
    x=int(input('Digite o número desejado: '))
listaf=[]
for e in range (0,len(lista),-1):
    listaf.append(e)