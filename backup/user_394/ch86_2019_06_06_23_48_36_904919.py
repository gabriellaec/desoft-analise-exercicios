with open('dados.csv','r') as arquivo:
    conteudo = arquivo.read()
novo_conteudo = conteudo.replace(",","	")
with open('dados.csv','w') as arquivo:
    arquivo.write(novo_conteudo)