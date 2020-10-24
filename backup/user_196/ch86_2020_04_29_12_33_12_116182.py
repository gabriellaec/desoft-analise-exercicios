with open("dados.csv","r") as arquivo:
    conteudo = arquivo.read()
    conteudo.replace(",","\t")
    with open("dados.tsv","w") as novoarquivo:
        novoarquivo.write("conteudo")