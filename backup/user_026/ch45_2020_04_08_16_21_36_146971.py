numeros=int(input("digite um número inteiro positivo: "))
i=0
while i < len(numeros):
    numeros[len(numeros)-1]=i
    if numeros[i]==0 or numeros[i]<0:
        print(numeros)
    numeros=int(input("digite um número inteiro positivo: "))
    i+=1
        