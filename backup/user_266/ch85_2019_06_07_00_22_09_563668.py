with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.lower()
    lista_palavras = conteudo.split()
    cont = 0
    for e in lista_palavras:
        if e == 'banana':
        	cont += 1
    print(cont)