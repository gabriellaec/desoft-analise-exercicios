def custo_passagem(km):
    if km<=200:
        custo=0.50*km
    else: custo=0.50*200+(km-200)*0.45
    return custo
km=float(input("Entre com a distância que deseja percorrer, em KM: "))
print(custo_passagem(km))