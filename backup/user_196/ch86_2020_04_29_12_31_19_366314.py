with open("dados.csv","r") as arquivo:
    conteudo = arquivo.read()
    conteudo.replace(",","\t")
        