with open("dados.csv", "r") as arquivo:
    conteudo = arquivo.read().replace(",","	")
    with open("dados.tsv", "w") as arquivo_novo:
        arquivo_novo.write(conteudo)
 