pica = True
lista = []
while pica:
    numero = int(input('Insira um número inteiro positivo! (0 ou negativo para parar): '))

    if numero > 0:
        lista.append(numero)
    else:
        pica = False

i = len(lista)-1

while i >= 0:
    print(lista[i])
    i-=1

