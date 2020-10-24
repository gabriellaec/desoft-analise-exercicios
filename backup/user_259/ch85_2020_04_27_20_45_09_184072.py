with open('macacos-me-mordam.txt', 'r') as arquivo:
    contador = 0
    palavras = arquivo.read()
    palavras.upper()
    tudo = palavras.split()
for b in tudo:
    if b=='BANANA':
        contador+=1
print(contador)