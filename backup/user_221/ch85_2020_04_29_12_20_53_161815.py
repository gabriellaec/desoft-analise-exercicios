with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    c = 0
    i = 0
    while i < len(palavras):
        if palavras[i].upper() == 'BANANA':
            c += 1
            i += 1
        else:
            i +=1
print(c)