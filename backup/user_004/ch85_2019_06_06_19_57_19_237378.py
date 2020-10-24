with open('macacos-me-mordam.txt', 'r') as arq:
    texto=json.read(arq)
    textonovo=texto.lower()
    print(textonovo.count('banana'))
    
    