with open('dados.csv','r') as arquivo1:
    cc = arquivo1.read()
    ac = cc.replace(',','\t')
    with open('dados.tsv','w') as arquivo2:
        arquivo2.write(ac)