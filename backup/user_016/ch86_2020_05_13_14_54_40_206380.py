with open('dados.csv','r') as arquivo:
    conteudo = arquivo.read()
    trocar = conteudo.replace('c', '	')
print(trocar)