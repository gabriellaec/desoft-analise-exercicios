with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
conteudo=conteudo.split()
ocorrencias = 0
for i in conteudo:
    i=i.lower()
    if i == 'banana':
        ocorrencias += 1
print(ocorrencias)