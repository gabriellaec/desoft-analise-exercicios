with open('dados.csv','r') as arquivo:
    conteudo = arquivo.read()
novo_conteudo = conteudo.replace(",","	")
with open('dados.csv','w') as arquivo:
    novo_conteudo = arquivo.write()