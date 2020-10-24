with open("dados.csv", "r") as csv, open("dados.tsv". "w") as tsv:
    conteudo_csv=csv.read()
    lista_csv=conteudo_csv.split()
    for i in lista_csv:
        elemento=str(i)
        tsv.write(elemento)
        tsv.write("	")