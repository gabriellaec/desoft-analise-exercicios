with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()

lista = conteudo.split()

contador = 0

for palavra in lista:
    if palavra.upper() == 'BANANA':
        contador += 1
        
print(contador)