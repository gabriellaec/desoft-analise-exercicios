with open("macacos-me-mordam.txt","r")as arquivo:
    conteudo = arquivo.read()
    frase = conteudo.upper()
    contador = 0
    lista = frase.split()
    for c in lista:
        if c == "banana":
            contador+=1
        print(contador)