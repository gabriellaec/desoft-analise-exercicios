valor=int(input('digite um numero: '))
numeros=[]
while valor>0:
    numeros.append(valor)
    valor=int(input('digite um numero: '))
inverso=[]
i=len(numeros)-1
while i>=0:
    inverso.append(numeros[i])
    i-=1
print(inverso)