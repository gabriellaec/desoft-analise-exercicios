with open('macacos-me-mordam.txt', 'r') as arquivo:
    n_ocorrencias = 0
    texto = arquivo.read()
    lista_palavras = texto.split()
    for e in lista_palavras:
        if e.upper() = 'BANANA':
            n_ocorrencias += 1
    print(n_ocorrencias)
    
    
