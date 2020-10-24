lista = []
programa = True
while programa:
    numeros = int(input('digite um número inteiro: '))
    if numeros <= 0:
        programa = False
    else:
        lista.append(numeros)
        
lista_2 = []
i = len(lista)-1

while i >= 0:
    lista_2.append(lista)
    i = i - 1
    
