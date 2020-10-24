with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

conteudo_final = conteudo.split()
c = 0

for palavra in conteudo_final:
    c += 1

print(c)