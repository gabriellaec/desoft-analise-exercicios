dist = int(input('Qual a distancia de sua viajem?: '))
if dist <= 200:
    preco = dist * 0.5
    print(preco).2f
elif dist > 200:
    dist -= 200
    preco = dist * 0.45
    preco += 100
    print(preco).2f
    