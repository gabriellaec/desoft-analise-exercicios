with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
lista = conteudo.split(' ' or '\n')
print(lista)
print(len(lista))