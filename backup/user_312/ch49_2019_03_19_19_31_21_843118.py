lista=[]
lista_invertida=[]
contador=-1 #quando for inserido o primeiro valor o ponteira será 0
numero=1
while numero>0:
    numero=int(input("digite um numero inteiro positivo ou um numero menor ou igual a zero para finalizar:"))
    if numero>0:
        lista.append(numero)
        contador = contador + 1
while contador>=0:
    lista_invertida.append(lista[contador])
    contador = contador - 1
print(lista_invertida)
