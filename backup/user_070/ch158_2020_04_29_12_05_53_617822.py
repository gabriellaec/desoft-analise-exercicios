with open('texto.txt','r') as texto:
    conteudo = texto.read()
lista = conteudo.split()
print(len(lista))