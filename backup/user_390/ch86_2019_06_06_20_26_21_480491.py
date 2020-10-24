with open("dados.csv","r") as arquivo:
    conteudo= arquivo.read()
	conteudo.replace(",","")
with open("dados.tsv","w") as tsv:
    tsv.write(conteudo)