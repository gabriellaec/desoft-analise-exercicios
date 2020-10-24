# Guarda conteudo do arquivo em uma string
with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    novo_conteudo = conteudo.replace(',', '	')

# Cria dados.tsv com novo_conteudo
with open('dados.tsv', 'w') as dados:
    dados.write(novo_conteudo)