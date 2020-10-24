def preco_da_passagem(km):
    if km<=200:
        return(0.5*km)
    elif km>200:
        return(0,45*km)

print(preco_da_passagem)