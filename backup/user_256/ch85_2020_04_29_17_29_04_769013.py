open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split()
    contador = 0
    for palavras in lista:
        if palavras == 'Banana' or palavras == 'BANANA' or palavras == 'BaNaNa' or palavras == 'banana':
            contador+=1
    print (contador)