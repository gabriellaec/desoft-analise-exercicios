def faixa_notas(lista_notas):
    x=0
    y=0
    z=0
    for nota in lista_notas:
        if nota<5:
            x+=1
        elif 5<=nota<=7:
            y+=1
        else:
            z+=1
    lf = [x,y,z]
    return lf