def verifica_preco(x,y,z):
    for x in y:
        for y, valor in z.items():
            if valor == 10:
                return valor*2
            elif valor == 20:
                return valor*2
            else:
                return valor/4
    