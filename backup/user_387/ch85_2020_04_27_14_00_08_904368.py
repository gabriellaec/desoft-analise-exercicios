with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()

c = 0
for word in palavras:
    if str.lower(word) == 'banana':
        c+=1

print(c)