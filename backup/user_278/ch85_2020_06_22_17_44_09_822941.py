with open ('macacos-me-mordam.txt', 'r' ) as arquivo:
    conteudo = arquivo.read()
    frase = conteudo.lower()
    fasee = frase.split()
    contador = 0
    for c in frasee:
        if c == 'banana':
            contador += 1
print (contador)