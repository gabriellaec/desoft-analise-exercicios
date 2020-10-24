def palavras(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        lista = conteudo.split()
        return lista

palavra = palavras('macacos-me-mordam.txt')
bananas = []

i = 0
while i < len(palavra):
    if palavra[i].upper == 'BANANA':
        bananas.append(palavra[i])
    i+=1
        
print(len(bananas))


