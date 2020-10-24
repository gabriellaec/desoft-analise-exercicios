with open ("dados.cvs", "r") as cvs:
    conteudo = cvs.read().replace(",", " ")
    with open ("dados.tvs", "w") as tvs:
        tsv.write(conteudo)