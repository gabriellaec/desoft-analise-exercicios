arquivo = open("dados.csv", 'r')
conteudo = arquivo.read()
converte = conteudo.replace(",", '\t')
print(converte)