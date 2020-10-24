with open('palavras.txt','a') as arquivo:
    conteudo = arquivo.read()
    
lista_de_palavras = conteudo.split()

print(len(lista_de_palavras))