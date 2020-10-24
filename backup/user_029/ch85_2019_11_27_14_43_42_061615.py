with open('macacos-me-mordam.txt','r')as arquivo:
    conteudo = arquivo.readlines()
    #separado = conteudo.split(',')

contador = 0
for i in separado:
    i.lower()
    if i == 'banana':
        contador += 1
    print(i)
print(contador)