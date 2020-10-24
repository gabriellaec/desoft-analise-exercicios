with open('macacos-me-mordam.txt', 'r') as texto:
    conteudo = texto.read()
    conteudo = conteudo.split()
lista = ['Banana','banana','BANANA','BaNaNa']   
cont = 0
for i in conteudo:
    if i in lista:
        cont += 1
print (cont)