km=float(input('quantos quilômetros são a viagem?'))
def valor_da_passagem(km):
    if km<=200:
        valor=km*0.5
    else:
        valor=km*0.45
    return valor

print('{0:.2f}'.format(valor_da_passagem(km)))