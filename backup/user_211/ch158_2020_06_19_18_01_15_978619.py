with open('texto.txt','r') as arquivo:
    conteudo=arquivo.rad()
    palavras=conteudo.split()
    n=0
    for i in range(0,len(palavras)):
        n+=1
    print(n)
    