with open("macacos-me-mordam.txt","r")as arquivo:
    conteudo = arquivo.read()
    frase = conteudo.upper()
    contador = 0
    for c in frase.split():
        if c == "banana":
            contador+=1
    print(contador)