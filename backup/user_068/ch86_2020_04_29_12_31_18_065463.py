with open('dados.csv', 'r') as arquivo:
    conteudo_completo = arquivo.read()
    conteudo_completo.replace(',', "\t")
   
    