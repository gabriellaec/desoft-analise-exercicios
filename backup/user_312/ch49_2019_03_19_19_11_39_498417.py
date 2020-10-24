lista=[]
lista_invertida=[]
contador=0
numero=0
while lista[i]<=0:
    numero=int(input("digite um numero inteiro positivo ou um numero menor ou igual a zero para finalizar:"))
    if numero>0:
        lista.append(numero)
    contador+=1
while contador!=0:
    lista_invertida.append(lista[contador])
    contador-=1
print(lista_invertida)
