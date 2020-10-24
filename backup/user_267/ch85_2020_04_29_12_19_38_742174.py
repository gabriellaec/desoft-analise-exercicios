with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read().lower()
    lista = conteudo.split()
    contador = 0
    for i in range(len(lista)):
        if lista[i] == 'banana':
            contador += 1
    print(contador)
