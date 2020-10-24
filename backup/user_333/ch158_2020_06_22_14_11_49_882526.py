with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

lista_letras = conteudo.split()
print(len(lista_letras))