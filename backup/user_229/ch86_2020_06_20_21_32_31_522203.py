with open('dados.csv', 'r') as em_csv:
    conteudo = em_csv.read()
    
print(conteudo.replace(',', '\t')