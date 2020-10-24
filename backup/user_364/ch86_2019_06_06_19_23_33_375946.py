with open ("dados.csv","r") as arquivo:
    conteudo=arquivo.read()
    
novo_arquivo= ("dados.csv").replace("csv","tsv")

with open ("dados.tsv", "w") as f:
    f.write(novo_arquivo)