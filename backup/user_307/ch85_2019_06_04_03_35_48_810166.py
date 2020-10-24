import re

with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
arc = str(conteudo)

lista_bananas=re.findall(r'(B|b)(A|a)ww(N|n)(A|a)',arc)

print(len(lista_bananas))