distancia = int(input( 'Quantos km voce percorre ? '))
def quantidade_km (x):
    if x<=200 :
        return x*0.5
        
    else:
        return x*0.95
custo = (quantidade_km(distancia)) 
print (' O preco da passagem eh {0:.2f}'.format(custo))
