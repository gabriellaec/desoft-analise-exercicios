distancia = int(input('Que distância deseja percorrer? '))
def calculo_da_passagem(distancia):
    if distancia>=200:
        preço = distancia*0.5
        print('A passagem custara {0:.2f}'.format(preço))
    else:
        preço = distancia*0.45
        print('A passagem custara {0:.2f}'.format(preço))
    return 'a'
calculo_da_passagem(distancia)