def calcula_preco_passagem (x):
    if (x<=200):
        return x * 0.50 
    else:
        return ((x-200) * 0.45) + (200 * 0.50)

x = int(input('Qual distância você deseja percorrer, em km?'))
print ('o valor da sua passagem será R$ {:.2f}'.format(calcula_preco_passagem(x)))