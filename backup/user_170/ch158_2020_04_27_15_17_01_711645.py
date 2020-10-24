with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
lista = conteudo.split(' ')
print(lista)
print(len(lista))