with open("texto.txt","r") as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split() # é uma lista
    print (len(palavras))