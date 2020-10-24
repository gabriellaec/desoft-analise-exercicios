with open('dados.csv','r') as CSV:
    dados = CSV.read()
    TSV = dados.replace(",","\t")
with open('dados.tsv','r') as novo_arq:
    novo_arq.write(TSV)
print(novo_arq)