with open('dados.csv.txt','r') as arq:
    dados = arq.readlines()
    for e in dados:
        tsv = e.replace(",","\t")
        print(tsv)