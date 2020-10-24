with open("macacos-me-mordam.txt", 'r') as arquivo:
    cont = 0
    for line in arquivo:
        palavras = line.split()
        for palavra in palavras:
            print(palavra)
            if palavra.lower() == 'banana'.lower():
                cont += 1
print(cont)