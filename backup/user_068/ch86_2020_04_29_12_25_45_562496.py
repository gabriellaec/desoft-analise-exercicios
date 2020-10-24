with open('dados.csv', 'r') as arquivo:
    conteudo_completo = arquivo.read()
    with open('dados.tsv', 'w') as arquivonovo:
        arquivonovo.write('conteudo_completo')
    