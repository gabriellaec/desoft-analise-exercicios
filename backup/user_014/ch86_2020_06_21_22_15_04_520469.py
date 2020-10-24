with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    todo_conteudo = conteudo.split('/t')
    arquivo[dados.tsv] = todo_conteudo