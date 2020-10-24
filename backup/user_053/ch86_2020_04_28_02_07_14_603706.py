import re

with open("dados.csv", 'r') as arquivo:
with open("dados.csv", 'w') as csv_arquivo:
for line in arquivo:
    conteudo = re.sub(",", "	", line)
    csv_arquivo.write(conteudo)