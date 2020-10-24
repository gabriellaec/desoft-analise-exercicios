with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)
conteudo = conteudo.casefold()
palavras = conteudo.split()
c = 0
for word in palavras:
    if word == 'banana':
        c+=1
print(c)