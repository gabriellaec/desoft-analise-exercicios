with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    lower = conteudo.lower()
    split = lower.split()
    cont = 0
    for e in split:
        if 'banana' in split:
        	cont += 1
    print(cont)