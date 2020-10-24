with open("dados.csv","r") as arquivo:
    conteudo = arquivo.read()
novo_conteudo = conteudo.replace(",","	")

with open("dados.tsv","w") as arquivo2:
    arquivo2.write(novo_conteudo)