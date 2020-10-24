with open('dados.tsv','w') as archive:
    with open('dados.csv','r') as arquivo:
        conteudo=arquivo.read
        x=conteudo.replace(',','\t')
        archive.write(x)