with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    texto = conteudo.upper()
    lista = texto.split()
    for i in lista:
        s = 0
        if i == 'BANANA':
            s+=1
        print(s)