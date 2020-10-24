import os
file = 'dados.csv'
novofile= os.path.splitext(file)[0]
os.rename(file, novofile + '.tsv')