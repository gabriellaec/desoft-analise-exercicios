with open('dados.csv', 'r') as arquivo:
        conteudo = arquivo.read()
        junta = conteudo.split()
        separa = '\t'.join(junta)
with open('dados.tsv', 'w') as arquivo2:
        arquivo2.writelines(separa)
  
