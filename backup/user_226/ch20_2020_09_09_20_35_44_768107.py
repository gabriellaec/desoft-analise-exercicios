distancia = int(input("Quantos km voce vai percorrer? "))

def imprime_preco_passagem(distancia):
    float(distancia)
    if distancia < 200:
        preco = distancia * 0.5
        print(f"{preco:.2f}")
    else:
        preco = (200 * 0.5) + (distancia - 200) * 0.45
        print(f'{preco:.2f}')

imprime_preco_passagem(distancia)