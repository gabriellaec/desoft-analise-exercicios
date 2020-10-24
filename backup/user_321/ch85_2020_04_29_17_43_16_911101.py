with open('macacos_me_mordam.txt', 'r') as texto:
    conteudo = texto.read()
lista = ['Banana','banana','BANANA','BaNaNa']
cont = 0    
for i in conteudo:
    if i in lista:
        cont +=1