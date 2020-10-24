with open("dados.csv","r") as csv:
    conteudo = csv.read()
    switch = conteudo.replace(",", " ")
    with open("dados.tsv","w") as tsv:
        x = tsv.write(switch)
        print(x)
