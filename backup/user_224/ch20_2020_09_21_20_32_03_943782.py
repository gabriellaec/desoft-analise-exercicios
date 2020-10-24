DISTANCIA_A_PERCORRER = int(input('Qual distancia você pretende percorrer em km?  '))

if DISTANCIA_A_PERCORRER <= 200 :
    def preço_da_passagem(DISTANCIA_A_PERCORRER) :
        Total = DISTANCIA_A_PERCORRER*0.50
        return Total
if DISTANCIA_A_PERCORRER > 200 :
    def preço_da_passagem(DISTANCIA_A_PERCORRER) :
        Total = 200*0.50 + (DISTANCIA_A_PERCORRER - 200)*0.45
        return Total


Total = preço_da_passagem(DISTANCIA_A_PERCORRER)
print('O preço da passagem é {0:.2f}'.format(Total))