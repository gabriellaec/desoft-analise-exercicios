with open("dados.csv", "r") as arquivo:
    conteudo = arquivo.read()
with open("dados.tsv", "a") as arquivo2:
    b= conteudo.replace(",","	")
    l = arquivo2.write(b)