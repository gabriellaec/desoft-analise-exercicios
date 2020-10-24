def inverte_lista(lista):
    invertida = []
    contador = len(lista) -1
    while contador >= 0:
        invertida.append(lista[contador])
        contador -= 1
    return invertida

lista = []
positivo = True
while positivo:
    numero = int(input("Digite um número: "))
    if numero < 1:
        positivo = False
    else:
        lista.append(numero)
print(inverte_lista(lista))