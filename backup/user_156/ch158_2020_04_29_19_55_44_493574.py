with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
    conteudo_separado = conteudo.split()
    
    print(len(conteudo_separado))
    