with open ("dados.csv","r") as arquivos:
    conteudo = arquivo.read()
print(conteudo.replace(",","\t")