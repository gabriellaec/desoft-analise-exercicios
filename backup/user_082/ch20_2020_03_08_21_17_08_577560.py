def preco_da_passagem(km):
    if km<=200:
        preco1= km * 0.50
        return (float(preco1))
    elif km>200:
        preco2= (km-200) * 0.45 + 100.00
        return (float(preco2))