def palavras(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        lista = conteudo.split()
        return lista

palavra = palavras('macacos-me-mordam.txt')
bananas = list()

for i in range(len(palavra)):
    if palavra[i].upper == 'BANANA':
        bananas.append(palavra[i])
        
print(len(bananas))


