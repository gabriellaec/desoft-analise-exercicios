with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    todo_conteudo = conteudo.replace(',', '/t')
    
with open('dados.tsv', 'w') as arquivo_2:
    arquivos_2.write(todo_conteudo)