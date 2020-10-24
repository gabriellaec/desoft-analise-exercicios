with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()

conteudo2 = conteudo.lower()
conteudo_final = conteudo2.split()
s = 0

for palavra in conteudo_final:

    if palavra == 'banana':
        s += 1

print(s)
    