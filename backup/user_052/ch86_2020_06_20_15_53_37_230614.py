with open ("dados.csv", "r") as arquivo:
    ler = arquivo.read()

    x = ler.replace(",", "	")

with open ("dados.tsv", "w") as arquivo2:
    escrever = arquivo2.write(x)