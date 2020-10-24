with open('dados.csv','r') as arquivo:
    counteudo = arquivo.read()
    trocar = conteudo.replace('\c', '\t')
print(trocar)