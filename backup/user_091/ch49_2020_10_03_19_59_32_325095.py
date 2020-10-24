numeros=[]
while True:
    lista_nova=[]
    x=int(input('Digite números inteiros positivos( negativo ou zero para sair): '))
    if x<=0:
        break
    numeros.append(x)

i=1
while i<=len(numeros):
    lista_nova.append(numeros[-i])
    i+=1
    
print(lista_nova)
