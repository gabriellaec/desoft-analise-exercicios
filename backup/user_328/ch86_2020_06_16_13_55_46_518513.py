with open('dados.csv', 'r') as arquivo:
    conteudo= arquivo.read()
    with open('dados.tsv', 'w') as arquivo:
        conteudo= conteudo.replace(',', '  ')
        arquivo.write(conteudo)
        
    #print(conteudo)