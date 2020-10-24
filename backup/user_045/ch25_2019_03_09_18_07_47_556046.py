def passagem(km):
    if km>200:
        y=100 + km*0.45
    else:
        y=km*0.50
    return y
km=int(input('distancia?'))
print(passagem(km))