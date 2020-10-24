contador = 0

with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

lista = list(conteudo)
for a in lista:
    if a != ' ':
        contador += 1

print(contador)