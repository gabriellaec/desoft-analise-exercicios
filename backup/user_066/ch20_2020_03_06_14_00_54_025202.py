distancia = float(input('Que distância deseja percorrer? '))
def calculo_da_passagem(distancia):
    if distancia<=200:
        preco = distancia*0.5
        print('A passagem custara R${0:.2f}'.format(preco))
    else:
        preco = (distancia-200)*0.45+100
        print('A passagem custara R${0:.2f}'.format(preco))
    return 'a'
calculo_da_passagem(distancia)