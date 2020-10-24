with open('macacos-me-mordam.txt', 'r') as arquivo:
    contador = 0
    palavras = arquivo.read()
    palavras = palavras.upper()
    palavras = palavras.split()
for b in palavras:
    if b=='BANANA':
        contador+=1
print(contador)
print(palavras)