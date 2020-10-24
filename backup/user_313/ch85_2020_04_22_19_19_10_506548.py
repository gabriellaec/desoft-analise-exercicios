with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavra = conteudo.split()

lista = list()
for i in palavra:
    x = i.lower()
    lista.append(x)
    
print(len(lista))
    