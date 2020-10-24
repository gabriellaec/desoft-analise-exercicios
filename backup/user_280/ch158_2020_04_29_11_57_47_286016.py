with open('texto.txt', 'r') as arquivo:
    lista = arquivo.split()
quantidade = len(lista)
print(quantidade)