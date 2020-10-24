with open('macacos-me-mordam.txt', 'r') as arquivo:
    low=arquivo.low()
    ocorrencias=0
    lista=low.split()
    for i in lista:
        if i =='banana':
            ocorrencias+=1
    print(ocorrencias)
        