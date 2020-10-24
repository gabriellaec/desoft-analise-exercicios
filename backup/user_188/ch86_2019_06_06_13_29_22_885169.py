with open("dados.csv", "r", encoding = "utf8") as arquivo_CSV:
    conteudo = arquivo_CSV.read()
    
troca = conteudo.replace(",","\t")

with open("dados.tsv", "w", encoding = "utf8") as arquivo_TSV:
    arquivo_TSV.write(troca)