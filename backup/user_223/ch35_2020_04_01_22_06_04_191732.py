while True:
    numero_perguntado = int(input('Escolha um numero inteiro: '))
    lista1 = []
    while numero_perguntado != 0:
        lista1.append(numero_perguntado)
        numero_perguntado = int(input('Escolha um numero inteiro: '))
    if numero_perguntado == 0:
        lista1_soma = sum(lista1)
        print(lista1_soma)
        break
    else:
        numero_perguntado = int(input('Escolha um numero inteiro: '))