with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    lista = texto.split(' ', ',')
    i = 0
    for i in lista:
        i += 1
    print(lista)