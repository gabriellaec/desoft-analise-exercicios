with open('macacos-me-mordam.txt', 'r') as arquivo:
    leitura = arquivo.read()
    leitura = leitura.lower

count = 0
for elemento in leitura:
    if elemento == 'banana':
        count +=1