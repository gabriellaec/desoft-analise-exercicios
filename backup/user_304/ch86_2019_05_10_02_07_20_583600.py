with open ('dados.csv', 'r') as arquivo:
        conteudo=arquivo.read()
    
lista=conteudo.splint(',')

saida= '\t'.join(lista)
print(saida)

with open('dados.tsv', 'w') as arquivo:
    arquivo.white(saida)