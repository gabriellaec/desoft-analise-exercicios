import re

with open("dados.csv", 'r') as arquivo:
with open("dados.txt", 'w') as csv_arquivo:
for line in arquivo:
    conteudo = re.sub(",", "\t", line)
    csv_arquivo.write(conteudo)