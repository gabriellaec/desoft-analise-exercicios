def calcula_total_da_nota (preço, quantidade):
    nota = []
    for i in preço and in quantidade:
        valor = preço[i]*quantidade[i]
        nota.append(valor)
        return nota
    