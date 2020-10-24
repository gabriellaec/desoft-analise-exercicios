with open('macacos-me-mordam.txt','r') as arquivo:
    leitura = arquivo.read()
    palavras = leitura.split()
    i = 0
    for x in palavras:
        if x.lower() == 'banana':
            i+=1
print(i)