def verifica_preco(title, colors, price):
    for i,j in colors.items():
        if i == title:
            cor = j
            break
    for i,j in price.items():
        if i == cor:
            return j
        