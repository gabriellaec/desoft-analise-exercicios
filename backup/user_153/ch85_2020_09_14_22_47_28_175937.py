with open("macacos-me-mordam.txt", 'r', encoding="utf8") as arquivo:
    cont = 0
    for line in arquivo:
        palavras = line.split()
        for palavra in palavras:
            if palavra.lower() == 'banana'.lower():
                cont += 1