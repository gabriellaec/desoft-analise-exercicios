numeros=int(input("digite um número inteiro positivo: "))
lista=[]
while numeros>0:
    lista.append(numeros)
    numeros=int(input("digite um número inteiro positivo: "))
    
print(lista[::-1])
