with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    
with open('dados.csv', 'w') as arquivo:
    arquivo.write(conteudo.replace(',','\t'))
    
    



