with open(dados.csv,"r") as arq:
    conteudo = arq.read().replace(",", " ")
    with open(dados.tsv, "w") as arq2:
        arq2.write = conteudo
