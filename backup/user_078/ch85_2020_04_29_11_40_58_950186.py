with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
lista_palavras = conteudo.split()

bananas=0
for i in lista_palavras:
    if i == 'banana':
        bananas+=1
    elif i == 'BANANA':
        bananas+=1
    elif i == 'BaNaNa':
        bananas+=1
    elif i == 'Banana':
        bananas+=1
    else:
        bananas=bananas
