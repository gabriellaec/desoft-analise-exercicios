with open('macacos-me-mordam.txt', 'r') as arq:
    texto=json.load(arq)
    textonovo=texto.lower()
    print(textonovo.count('banana'))
    
    