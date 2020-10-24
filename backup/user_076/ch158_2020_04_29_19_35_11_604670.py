with open ('texto.txt','r') as arquivo:
    conteúdo = arquivo.read()
    lista_de_palavras = conteúdo.split()

print (len(lista_de_palavras))