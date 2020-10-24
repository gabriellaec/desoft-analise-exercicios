with open('dados.csv', 'r') as arquivo:
    conteudo_completo = arquivo.read()
    b = conteudo_completo.replace(',', "	")
    with open("dados.tsv", "w") as novoarquivo:
        novoarquivo.write(b)
   
    