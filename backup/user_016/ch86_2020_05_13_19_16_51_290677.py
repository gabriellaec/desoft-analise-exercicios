with open('dados.csv','r') as arquivo:
    conteudo = arquivo.read()
    troca = conteudo.replace(',','	')
    with open('dados.tsv','w') as arquivo2:
        conteudo2 = arquivo2.write(troca)
