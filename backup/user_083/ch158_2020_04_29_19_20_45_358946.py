with open('texto.txt','r') as arquivo:
    conteudo=arquivo.read()
    palavras=conteudo.split()
    print (len(palavras))