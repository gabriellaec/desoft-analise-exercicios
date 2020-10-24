with open('macacos-me-mordam.txt','r') as arquivo:
    texto = arquivo.read().lower()
    ocorrencias = 0
    lista = texto.split()
    for palavra in lista:
        if palavra == 'banana':
            ocorrencias += 1
    print(ocorrencias)
            
