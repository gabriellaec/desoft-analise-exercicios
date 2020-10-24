with open ("dados.csv", "r") as arquivo:
    ler = arquivo.read()
    replace = ler.replace(",","\t")
with open ("dados.tsv", "w") as arquivo2:
    write = arquivo2.write(replace)
    