with open ('dados.csv', 'r') as arquivo:
    conteudo_csv = arquivo.read()

conteudo_tsv = conteudo_csv.replace(',','	')
print (conteudo_tsv)
    
    