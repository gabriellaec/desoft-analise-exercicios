with open("dados.csv",'a') as arquivo:
    dados = arquivo.read()
    for i in dados:
        "dados.tsv" = i.replace(', ', '	')
print("dados.tsv")