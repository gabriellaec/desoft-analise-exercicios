with open("dados.csv", "r") as csv:
    lista_linhas_tsv=[]
    for line in csv:
        modificada=line.replace(",", "\t")
        lista_linhas_tsv.append(modificada)
with open('dados.tsv', 'w') as tsv:
    for line in lista_linhas_tsv:
        conteudo_tsv=tsv.writelines(line)