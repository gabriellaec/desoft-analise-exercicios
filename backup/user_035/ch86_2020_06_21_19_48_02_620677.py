with open(dados.cvs,"r") as arq:
    conteudo = arq.read().replace(",", " ")
    with open(dados.tvs, "w") as arq2:
        arq2.write(conteudo)
