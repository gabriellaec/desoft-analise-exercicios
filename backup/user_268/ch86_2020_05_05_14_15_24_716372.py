import os
with open("dados.csv", 'r') as arquivo:
    leit = arquivo.read()
    novo = leit.replace(",", "\t")
    os.rename(novo, 'dados.tsv')
    
    