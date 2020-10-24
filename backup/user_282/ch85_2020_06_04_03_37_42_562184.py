with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split()
    count = 0
    for i in lista:
        if i.lower() == 'banana':
            count += 1
    print(count)