with open('dados.csv','r') as arquivo: 
    conteudo = arquivo.read()
novo_conteudo = conteudo.replace(",","\t")

with open('dados.csv', 'w') as f:
    f.write(novo_conteudo)