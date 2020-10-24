with open ('dados.csv','r') as arquivo:
    conteudo=arquivo.read()
    palavras=''
    for e in conteudo:
        if e == ',':
            palavras+="\t"
        else:
            palavras+=e
    print(palavras)
    with open ('dados.tsv','w') as arquivo2:
        arquivo2.write(palavras)