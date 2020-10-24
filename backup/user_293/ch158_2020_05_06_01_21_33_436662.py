with open('texto.txt','r') as arquivo:
    conteudo = arquivo.read()
    conteudo_final = conteudo.split()
    print(len(conteudo_final))