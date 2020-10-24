with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.lower()
    lista = conteudo.split()
    total = 0
    for item in lista:
        if item == 'banana':
            total += 1

print(total)