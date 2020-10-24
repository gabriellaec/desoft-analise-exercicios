import os
fo = open("dados.csv", 'r')
leit = fo.read()
novo = leit.replace(",", "	")
os.rename(novo, "dados.tsv")
fo.close()































