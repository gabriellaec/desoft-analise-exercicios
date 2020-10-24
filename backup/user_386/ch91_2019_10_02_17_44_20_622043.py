arquivo = open('palavras.txt','r')
conteudo = arquivo.readlines()
letra_a = []
for line in conteudo:
    palavras = line.split()
    for i in palavras:
        if i[0] == 'a' or 'A': 
            letra_a.append(i)
arquivo.close()
print(letra_a)
