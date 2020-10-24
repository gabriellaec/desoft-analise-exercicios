with open ('dados.csv', 'r') as arquivo:
    conteudo=arquivo.read()
    
    lista=conteudo.splint(',') 

saida=conteudo.replace(',','\t')
print(saida)

with open('dados.tsv', 'w') as arquivo:
    arquivo.white(saida)
