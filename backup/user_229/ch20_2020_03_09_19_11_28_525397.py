input ("Qual distância você deseja percorrer? Responda em km: "
def custo(km)
    if km < 200:
        return 0.50*km
    else:
        return 0.45*km
print(custo)