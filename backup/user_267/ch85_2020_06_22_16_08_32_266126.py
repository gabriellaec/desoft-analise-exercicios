with open(' macacos-me-mordam.txt','r') as arquivo:
    texto = arquivo.read()
    ocorrencias = 0
    for palavra in texto:
        palavra.lower()
        if palavra == 'banana':
            ocorrencias += 1
        return ocorrencias
            
