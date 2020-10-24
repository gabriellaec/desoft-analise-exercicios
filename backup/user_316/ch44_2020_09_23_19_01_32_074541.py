dicionario = {}
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# popular dicionário
for i in range(len(meses)):
    dicionario[meses[i]] = i + 1
    
entrada = input( "Nome do mês: " )
print( dicionario[entrada] )