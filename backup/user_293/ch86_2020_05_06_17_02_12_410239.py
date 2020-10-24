with open('dados.csv','r') as arq:
    dados = arq.read()
    tsv = dados.replace(",","\t")
with open('dados.tsv','r') as novo_arq:
    novo_arq.write(tsv)
print(novo_arq)