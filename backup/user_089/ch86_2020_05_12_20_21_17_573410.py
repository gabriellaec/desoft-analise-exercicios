with open("dados.csv","r") as arquivo:
    a = arquivo.read()
    x = a.replace(",","	")
with open("dados.tsv","w") as arquivo 2:
    arquivo2.write(x)
    