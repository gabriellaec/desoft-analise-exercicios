with open ("dados.csv", "r") as arquivo1:
    conteudo1=arquivo1.readlines()
with open ("dados.tsv", "a") as arquivo2:
    conteudo2 = conteudo1.replace(" ","    ")
    arquivo2.write(conteudo2)