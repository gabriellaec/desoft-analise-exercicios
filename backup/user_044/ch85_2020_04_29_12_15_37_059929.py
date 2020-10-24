with open('macacos-me-mordam.txt', 'r') as arquivo:
    arq=arquivo.read()
    low=arq.lower()
    ocorrencias=0
    lista=low.split()
    for i in lista:
        if i =='banana':
            ocorrencias+=1
    print(ocorrencias)
        