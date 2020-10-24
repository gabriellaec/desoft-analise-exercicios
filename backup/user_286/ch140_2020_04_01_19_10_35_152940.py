def faixa_notas(lista_notas):
    nota_menor_5 = 0
    nota_5_7 = 0
    nota_maior_7 = 0

    for nota in lista_notas:
        if nota < 5:
            nota_menor_5 += 1
        elif nota > 7:
            nota_maior_7 += 1
        else:
            nota_5_7 += 1
    
    lista_quantidades = [nota_menor_5, nota_5_7, nota_maior_7]
    return lista_quantidades