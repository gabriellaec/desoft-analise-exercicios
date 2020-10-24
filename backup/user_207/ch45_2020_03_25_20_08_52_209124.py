numeros =[]
i=0
X = True
while X:
    numeros.append(int(input("Digite um numero inteiro positivo")))
    if numeros[i]<=0:
        X=False
    i += 1
numeros.reverse()
print (numeros)