with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    todo_conteudo = conteudo.replace(',', '   ')
    
with open('dados.tsv', 'w') as arquivo_2:
    arquivo_2.write(todo_conteudo)