with open ('dados.csv', 'r') as arquivo:
    conteudo_csv = arquivo.read()

conteudo_tsv = conteudo_csv.replace(',','	')

with open ('dados.tsv', 'a') as arquivo2:
    arquivo2.write(conteudo_tsv)
    
    