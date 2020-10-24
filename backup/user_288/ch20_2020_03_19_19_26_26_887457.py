passageiro = int (input('Quantos km deseja percorrer?'))
if passageiro <= 200:
    preco_final = passageiro * 0.50
else:
    preco_final = (passageiro - 200)* 0.45 + 100
print ('Valor final da sua passagem é {0:.2f}'.format(preco_final))