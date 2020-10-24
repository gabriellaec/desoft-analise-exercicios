km=input('Qual distancia vc deseja percorrer? ')
def preco_da_passagem(km):
    if km<=200:
        preco1= km * 0.50
        return (f'{preco1:.2f}')
    elif km>200:
        preco2= (km-200) * 0.45 + 100.00
        return (f'{preco2:.2f}')
print(preco_da_passagem(250))