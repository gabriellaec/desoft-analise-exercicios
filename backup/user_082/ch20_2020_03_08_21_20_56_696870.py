def preco_da_passagem(km):
    if km<=200:
        preco1= km * 0.50
        return preco1
    print(f'{preco1:.2f}')
    elif km>200:
        preco2= (km-200) * 0.45 + 100.00
        return preco2
    print(f'{preco2:.2f}')