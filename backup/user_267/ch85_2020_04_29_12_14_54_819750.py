with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split()
    contador = 0
    for i in range(len(lista)):
        if lista[i] == 'banana' or lista[i] == 'Banana' or lista[i] == 'BaNaNa' lista[i] == 'BANANA'
            contador += 1
    print(contador)
