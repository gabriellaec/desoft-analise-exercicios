with open ("dados.csv","r") as arquivo:
    arquivo=arquivo.read()
    arquivo=arquivo.replace(",","	")
with open ("dados.tsv","w") as arquivo:
    arquivo.write(arquivo)
    