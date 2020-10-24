numeros=[]
while True:
    x=int(input('Digite números inteiros positivos( negativo ou zero para sair): '))
    if x<=0:
        break
    numeros.append(x)

i=1
while i<=len(numeros):
    print(numeros[-i])
    i+=1

                          

     