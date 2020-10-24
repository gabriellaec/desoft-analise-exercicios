with open ("dados.csv","r") as arquivo:
    arquivo=arquivo.read()
    a=arquivo.replace(",","	")
with open ("dados.tsv","w") as arquivo:
    arquivo.write(a)
    