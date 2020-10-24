def preco_da_passagem(km):
    if km<=200:
        preco1= km * 0.50
        return preco1
    elif km>200:
        preco2= (km-200) * 0.45
        return (preco1 + preco2)