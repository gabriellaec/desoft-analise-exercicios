with open("dados.csv", "r")as arquivo:
    conteudo=arquivo.read().replace(",", "	")
    with open("dados.tsv", "w")as arquivo2:
        arquivo2.write(conteudo)
        