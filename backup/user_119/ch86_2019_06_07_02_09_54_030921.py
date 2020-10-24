with open("dados.csv",'r') as arquivo:
    dados1 = arquivo.read()
    dados2 = dados1.replace(',', "	")
with open("dados.tsv",'w') as arquivo:
    arquivo.write(dados2)