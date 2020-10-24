with open ("dados.csv", "r") as arquivo1:
    conteudo1 = arquivo1.split()
    conteudo2 = ("    ".join(conteudo1))
with open ("dados.tsv", "w") as arquivo2:   
    arquivo2.write(conteudo2)