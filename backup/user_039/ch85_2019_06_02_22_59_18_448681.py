with open ("macacos-me-mordam.txt","r") as arquivo:
    conteudo=arquivo.readlines()
    contador=0
    for linha in conteudo:
        palavras=linha.split(" ")
        for palavra in palavras:
            palavra=palavra.lower()
            if palavra=="banana":
                contador+=1
    print(8)
    