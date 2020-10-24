with open("dados.csv","r") as arquivo:
    conteudo=arquivo.read()
with open("dados.tsv","w") as arquivo2:
    c=a.replace(",","\t")
    arquivo2.write(c)
    print(c)
