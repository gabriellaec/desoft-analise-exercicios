with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
lista_palavras = conteudo.split()

bananas=0
for i in lista_palavras:
    minusculo = i.lower()
    if minusculo == 'banana':
        bananas+=1
print (bananas)