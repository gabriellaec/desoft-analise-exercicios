with open("dados.csv","r") as arquivo:
    conteudo=arquivo.read()
with open("dados.tsv","w") as arquivo2:
    c=conteudo.replace(",","	")
    b=arquivo2.write(c)
