with open(texto, 'r') as arquivo:
    conteudo = arquivo.read()
    trocado = conteudo.replace(',', '	')
with open('dados.tsv', 'w') as arquivo2:
    arquivo2.write(trocado)


