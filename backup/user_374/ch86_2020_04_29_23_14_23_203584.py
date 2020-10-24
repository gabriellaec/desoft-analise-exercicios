def conta_palavras(teste):
    with open(teste, 'r') as arquivo:
        conteudo = arquivo.read()
        junta = conteudo.split()
        separa = '\t'.join(junta)

    with open('dados.tsv', 'w') as arquivo2:
        arquivo2.writelines(separa)
  
print(conta_palavras('dados.csv'))