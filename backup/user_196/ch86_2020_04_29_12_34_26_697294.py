with open("dados.csv","r") as arquivo:
    conteudo = arquivo.read()
    a=conteudo.replace(",","	")
    with open("dados.tsv","w") as novoarquivo:
        novoarquivo.write(a)