with open('dados.csv','w') as arquivo:
    arquivo.replace(',','    ')
    arquivo.replace('csv','tsv')