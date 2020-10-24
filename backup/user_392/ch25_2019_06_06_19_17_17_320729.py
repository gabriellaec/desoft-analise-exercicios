VIAGEM = int(inpu('qual é a distancia de sua viagem?'))

preco = 0

if VIAGEM <= 200:
    preco = VIAGEM * 0.5
else:
    preco = VIAGEM * 0.45
    