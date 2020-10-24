with open("dados.csv") as csv, open("dados.tsv") as tsv:
    conteudo_csv=csv.read()
    lista_csv=conteudo_csv.split()
    for i in lista_csv:
        tsv.writeline(i"\t")