with open ('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
lista_palavras = conteudo.split()

print (len(lista_palavras))

    
    