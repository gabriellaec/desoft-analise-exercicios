with open ("macacos-me-mordam.txt","r") as arquivo:
    conteudo=arquivo.readlines()
    contador=0
    for linha in conteudo:
        linha=linha.split(" ")
        for palavra in linha:
            palavra=palavra.lower()
            if palavra=="banana":
                contador+=1
    print(contador)
    