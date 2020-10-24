with open('dados.csv', 'r') as arquivo1:
    conteudo = arquivo1.read()
    troca = conteudo.replace(',', '\t')
with open('dados.tsv', 'w') as arquivo2:
    arquivo2.write(trocado)
    print('dados.tsv')
    
    