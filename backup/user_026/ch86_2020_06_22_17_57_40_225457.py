with open("dados.csv", "r") as arquivo:
    conteudo = arquivo.read().replace(",","\t")
    with open("dados.tsv", "w") as arquivo_novo:
        novo.write(conteudo)
 