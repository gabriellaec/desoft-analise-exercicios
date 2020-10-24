with open ("dados.csv", "r") as arquivo1:
    conteudo1=arquivo1.read()
    conteudo2 = conteudo1.replace(",","     ")
with open ("dados.tsv", "w") as arquivo2:   
    arquivo2.write(conteudo2)