with open('dados.csv','r', encoding = "utf8") as arquivo_CSV:
    conteudo = arquivo_CSV.read()
novo_conteudo = conteudo.replace(","," ")

with open('dados.tsv', "w", encoding = "utf8") as arquivo_TSV:
    arquivo_TSV.write(novo_conteudo)
    
    
    