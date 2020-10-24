valor=int(input('digite um numero: '))
numeros=[]
while valor>0:
    numeros.append(valor)
    valor=int(input('digite um numero: '))
inverso=[]
for i in numeros:
    inverso.append(i)
print(inverso)