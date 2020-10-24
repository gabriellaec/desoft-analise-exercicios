with open("dados.csv", "r") as arquivo:
    conteudo = arquivo.read()
    troca = conteudo.replace(",", " ")
    with open("dados.tsv", "w") as arquivo2:
        r = arquivo2.write(troca)
        print(r)
        print(conteudo)
