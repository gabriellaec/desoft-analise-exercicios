with open('macacos.txt','r')as arquivo:
    conteudo = arquivo.readlines()
contador = 0
palavra=[]
for i in conteudo:
    listaseparada = i.split(',')
    print(listaseparada)
    for i in range(len(listaseparada)):
        palavra.append(listaseparada[i].lower())
    for  i in palavra:
        if i == 'banana':
            contador += 1
print(contador)