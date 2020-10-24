with open ('macacos-me-mordam.txt', 'r') as arquivo:
    contador = 0
    conteudo = arquivo.read()
    lista = conteudo.split()
    for i in lista:
        if i.lower() == 'banana':
            contador += 1
    print(contador)
            
    