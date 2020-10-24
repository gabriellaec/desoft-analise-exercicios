km=input('Qual distancia vc deseja percorrer? ')
def preco_da_passagem(km):
    if km<=200:
        preco1= km * 0.50
        return ('{preco1:.2f}'.format)
    elif km>200:
        preco2= (km-200) * 0.45 + 100.00
        return ('{preco2:.2f}'.format)
