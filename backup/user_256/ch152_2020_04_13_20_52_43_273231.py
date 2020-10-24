def verifica_preco(title, nome, price):
    for a in nome:
        if a == title:
            color = nome[a]
    for z in price:
        if z==color:
            value=price[z]
    return value
    