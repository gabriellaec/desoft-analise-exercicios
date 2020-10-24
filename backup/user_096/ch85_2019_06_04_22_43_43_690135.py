with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    a = conteudo.lower()
    a.split()
    a.split(',')
    i = 0
    for e in a:
        if e == 'banana':
            i += 1
    
print(i)