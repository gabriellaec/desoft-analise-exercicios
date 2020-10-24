km=float(input('quantos km sua viagem vai ter? : '))

def kilometragem(km):
    if km<=200:
        y=km*0.5
        return y
    elif km>200:
        y=(200*0.5)+0.45*(km-200)
        return y
         