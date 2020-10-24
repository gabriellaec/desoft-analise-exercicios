VIAGEM = int(input('qual é a distancia de sua viagem?'))

preco = 0

if VIAGEM <= 200:
    preco = VIAGEM * 0.5
    print(preco)
else:
    preco = VIAGEM * 0.45
    print(preco)
    
  
    