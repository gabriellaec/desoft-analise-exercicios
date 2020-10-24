with open("dados.csv",'r') as arquivo:
    dados = arquivo.read()
    dados2 = dados.replace(', ', "	")
with open("dados.tsv",'w') as arquivo:
    arquivo.write(dados2)