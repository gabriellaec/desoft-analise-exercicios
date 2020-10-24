numeros=int(input("digite um número inteiro positivo: "))
lista=[]
while numeros>0:
    lista.append(numero)
    numeros=int(input("digite um número inteiro positivo: "))
    
i=0
invertida=[0]*len(lista)
while i<len(invertida):
    invertida[i]=lista[len(lista)-i]
    i+=1
    
    