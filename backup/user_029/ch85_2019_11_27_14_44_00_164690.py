with open('macacos-me-mordam.txt','r')as arquivo:
    conteudo = arquivo.readlines()

contador = 0
for i in conteudo:
    i.lower()
    if i == 'banana':
        contador += 1
    print(i)
print(contador)