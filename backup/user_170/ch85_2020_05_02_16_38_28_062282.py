with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
conteudo = conteudo.casefold()
palavras = conteudo.split()
print(palavras)
c = 0
for word in palavras:
    if word == 'banana':
        c+=1
print(c)