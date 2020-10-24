with open('dados.csv','r') as CSV:
    dados = CSV.read()
    TSV = dados.replace(",","	")
with open('dados.tsv','w') as novo_arq:
    novo_arq.write(TSV)
print(novo_arq)