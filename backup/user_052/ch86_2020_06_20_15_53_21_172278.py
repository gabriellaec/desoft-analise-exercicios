with open ("dados.csv", "r") as arquivo:
    ler = arquivo.read()

    x = ler.replace(",", "\t")

with open ("dados.tsv", "r") as arquivo2:
    escrever = arquivo2.write(x)