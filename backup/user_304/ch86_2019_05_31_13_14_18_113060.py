with open ('dados.csv', 'r') as arquivo:
    conteudo=arquivo.read()
    
    #lista=conteudo.split(',') 

saida=conteudo.replace(',','\t')
#print(saida)

with open('dados.tsv', 'w') as arquivo:
    arquivo.write(saida)
