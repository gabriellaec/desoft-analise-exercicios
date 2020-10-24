with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
lista = conteudo.split(' ')
print(lista)
print(len(lista))