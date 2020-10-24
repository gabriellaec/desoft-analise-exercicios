with open('macacos-me-mordam.txt', 'r') as arquivo:
    contador = 0
    palavras = arquivo.read()
    palavras = palavras.split(,',')
for b in palavras:
    b = b.upper()
    print(b)
    if b=='BANANA':
        contador+=1
print(contador)