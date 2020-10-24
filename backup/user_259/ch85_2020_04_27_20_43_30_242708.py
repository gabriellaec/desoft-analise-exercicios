with open('macacos-me-mordam.txt', 'r') as arquivo:
    contador = 0
    palavras = arquivo.read()
    palavras.upper()
for b in palavras:
    if b=='BANANA':
        contador+=1
print(contador)