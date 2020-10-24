with open('macacos-me-mordam.txt', 'r') as texto:
    conteudo = texto.read()
lista = ['Banana','banana','BANANA','BaNaNa']   
for i in conteudo:
    if i in lista:
        cont += 1
print (cont)