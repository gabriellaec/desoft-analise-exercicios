with open("dados.csv","r") as arquivo:
    conteudo = arquivo.read()
novo_conteudo = conteudo.reaplace(",","	")
with open("dados.tsv","w") as arquivo:
    arquivo.write(novo_conteudo)



    